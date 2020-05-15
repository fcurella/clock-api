import pytest

import freezegun

from alarms import models

pytestmark = pytest.mark.django_db


class TestAlarmsModels:
    def test_schedule(self):
        alarm = models.Alarm.objects.create(schedule="0 8 * * *",)

        assert alarm.task.crontab.hour == "8"
        assert alarm.task.crontab.minute == "0"

    @freezegun.freeze_time("2020-01-01 12:00:00", tick=True)
    def test_next_firing(self):
        alarm1 = models.Alarm.objects.create(schedule="0 8 * * *",)
        alarm2 = models.Alarm.objects.create(schedule="0 14 * * *",)

        # alarm2 should come first
        assert alarm2.next_firing < alarm1.next_firing

        with freezegun.freeze_time("2020-01-01 15:00:00", tick=True):
            assert alarm1.next_firing < alarm2.next_firing

        alarm1.schedule = "0 13 * * *"
        alarm1.save()
        assert alarm1.next_firing < alarm2.next_firing
