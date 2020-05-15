from django.contrib import admin

from . import models


@admin.register(models.Alarm)
class AlarmAdmin(admin.ModelAdmin):
    list_display = ("__str__", "timezone", "schedule", "active")
    list_filter = ("active",)


@admin.register(models.Sound)
class SoundAdmin(admin.ModelAdmin):
    pass
