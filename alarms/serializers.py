from rest_framework import serializers
from timezone_field import TimeZoneField as TimeZoneField_

from . import models


class TimeZoneField(serializers.ChoiceField):
    def __init__(self, **kwargs):
        choices = TimeZoneField_.CHOICES
        if kwargs.get("allow_blank"):
            choices += [(None, "")]
        super().__init__(choices, **kwargs)

    def to_representation(self, value):
        return str(super().to_representation(value))


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sound
        fields = ("id", "audio", "name")


class AlarmSerializer(serializers.ModelSerializer):
    sound = SoundSerializer()
    timezone = TimeZoneField()
    next_firing = serializers.DateTimeField()

    class Meta:
        model = models.Alarm
        fields = (
            "id",
            "schedule",
            "active",
            "custom_attributes",
            "timezone",
            "sound",
            "next_firing",
            "pre_fire",
            "post_fire",
        )
