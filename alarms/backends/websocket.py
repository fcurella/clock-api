from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .base import AlarmBackend


class WebSocketBackend(AlarmBackend):
    def __init__(self, *args, **kwargs):
        from alarms.serializers import AlarmSerializer

        super().__init__(*args, **kwargs)
        self.serializer = AlarmSerializer
        self.channel_layer = get_channel_layer()

    def group_send_json(self, msg):
        async_to_sync(self.channel_layer.group_send)("alarms", msg)

    def fire(self, alarm):
        msg = {
            "type": "alarms_fire",
            "message": self.serializer(instance=alarm).data,
        }
        self.group_send_json(msg)

    def publish(self, alarm):
        msg = {
            "type": "alarms_publish",
            "message": self.serializer(instance=alarm).data,
        }
        self.group_send_json(msg)

    def remove(self, alarm):
        msg = {
            "type": "alarms_remove",
            "message": self.serializer(instance=alarm).data,
        }
        self.group_send_json(msg)

    def stop(self, alarm):
        msg = {
            "type": "alarms_stop",
            "message": self.serializer(instance=alarm).data,
        }
        self.group_send_json(msg)

    def snooze(self, alarm):
        from alarms.tasks import fire

        self.stop(alarm)
        fire.apply_async((alarm.pk,), countdown=(9 * 60))
