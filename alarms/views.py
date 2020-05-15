from rest_framework import viewsets

from . import models, serializers


class AlarmViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = models.Alarm.objects.select_related("sound", "task__crontab").all()
    serializer_class = serializers.AlarmSerializer
    filterset_fields = ("active",)


class SoundViewSet(viewsets.ModelViewSet):
    queryset = models.Sound.objects.all()
    serializer_class = serializers.SoundSerializer
