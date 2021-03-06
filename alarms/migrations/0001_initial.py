# Generated by Django 3.0.5 on 2020-05-26 15:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_lifecycle.mixins
import model_utils.fields
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("django_celery_beat", "0012_periodictask_expire_seconds"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alarm",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("schedule", models.TextField()),
                (
                    "schedule_type",
                    models.CharField(
                        choices=[("crontab", "crontab")],
                        default="crontab",
                        max_length=20,
                    ),
                ),
                ("timezone", timezone_field.fields.TimeZoneField(default="UTC")),
                ("active", models.BooleanField(default=False)),
                (
                    "custom_attributes",
                    django.contrib.postgres.fields.jsonb.JSONField(
                        blank=True, default=dict
                    ),
                ),
                ("pre_fire", models.DurationField(blank=True, null=True)),
                ("post_fire", models.DurationField(blank=True, null=True)),
            ],
            options={"abstract": False,},
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Sound",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                ("name", models.CharField(default="", max_length=100)),
                ("audio", models.FileField(upload_to="")),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Interval",
            fields=[
                (
                    "alarm_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alarms.Alarm",
                    ),
                ),
                ("duration", models.DurationField()),
            ],
            options={"abstract": False,},
            bases=("alarms.alarm",),
        ),
        migrations.AddField(
            model_name="alarm",
            name="sound",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="alarms.Sound",
            ),
        ),
        migrations.AddField(
            model_name="alarm",
            name="task",
            field=models.OneToOneField(
                blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="django_celery_beat.PeriodicTask",
            ),
        ),
    ]
