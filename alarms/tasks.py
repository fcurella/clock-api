from config.celery_app import app

from alarms import models


@app.task
def fire(alarm_id):
    from alarms.backends.websocket import WebSocketBackend

    alarm = models.Alarm.objects.select_related("sound").get(pk=alarm_id)
    WebSocketBackend().fire(alarm)
