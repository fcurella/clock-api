import json
import uuid

from datetime import datetime, timedelta

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils import timezone

import freezegun
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django_lifecycle import LifecycleModel, hook
from model_utils.models import TimeStampedModel
from timezone_field import TimeZoneField

from .backends.websocket import WebSocketBackend


class Sound(TimeStampedModel):
    name = models.CharField(max_length=100, default="")
    audio = models.FileField()

    def __str__(self):
        return self.name


class ScheduleTypes(models.TextChoices):
    CRONTAB = "crontab", "crontab"
    # SOLAR = 'solar', 'solar'


class Alarm(LifecycleModel, TimeStampedModel):
    task = models.OneToOneField(PeriodicTask, on_delete=models.PROTECT, blank=True)
    schedule = models.TextField()
    schedule_type = models.CharField(
        max_length=20, choices=ScheduleTypes.choices, default=ScheduleTypes.CRONTAB,
    )
    timezone = TimeZoneField(default="UTC")
    sound = models.ForeignKey(Sound, on_delete=models.SET_DEFAULT, default=1)
    active = models.BooleanField(default=False)
    custom_attributes = JSONField(default=dict, blank=True)
    pre_fire = models.DurationField(null=True, blank=True)
    post_fire = models.DurationField(null=True, blank=True)

    def __str__(self):
        _crontab = crontab(*self.schedule.split())
        return f"{list(_crontab.hour)[0]:02}:{list(_crontab.minute)[0]:02}"

    def _get_schedule(self):
        schedule = CrontabSchedule.from_schedule(crontab(*self.schedule.split()))
        schedule.timezone = self.timezone
        if schedule.pk is None:
            schedule.save()
        return schedule

    @property
    def next_firing(self):
        with freezegun.freeze_time(timezone.now()):
            last_run = self.task.last_run_at
            if last_run is None:
                last_run = timezone.now()

            next_run = self.timezone.localize(
                self.task.schedule.remaining_estimate(last_run) + datetime.now()
            )
            previous = next_run - timedelta(days=1)
            if previous > timezone.now():
                next_run = previous

            return next_run

    @hook("before_create")
    def create_task(self):
        schedule = self._get_schedule()
        self.task = PeriodicTask.objects.create(
            crontab=schedule,
            name=f"{uuid.uuid4()}",
            task="alarms.tasks.fire",
            enabled=False,
        )

    @hook("after_create")
    def bind_task(self):
        self.task.args = json.dumps([self.pk])
        self.task.save()

    @hook("before_save", when="schedule")
    @hook("before_save", when="active")
    @hook("before_save", when="sound")
    def update_time(self):
        schedule = self._get_schedule()
        self.task.crontab = schedule
        self.task.enabled = self.active
        self.task.save()

    @hook("after_save")
    def publish(self):
        self.task.refresh_from_db()
        WebSocketBackend().publish(self)

    @hook("before_delete")
    def publish_delete(self):
        self.task.refresh_from_db()
        WebSocketBackend().remove(self)


class Interval(Alarm):
    duration = models.DurationField()

    @property
    def stop_time(self):
        with freezegun.freeze_time(timezone.now()):
            return self.next_firing + self.duration
