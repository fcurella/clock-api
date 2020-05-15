import pytest

from django.test import RequestFactory
from django.urls import reverse

import freezegun

from alarms import models, views
from clock.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    @freezegun.freeze_time("2020-01-01 12:00:00")
    def test_list(self, user: User, rf: RequestFactory):
        sound = models.Sound.objects.get(pk=1)
        alarm = models.Alarm.objects.create(schedule="0 8 * * *",)
        view = views.AlarmViewSet.as_view({"get": "list"})
        request = rf.get(reverse("api:alarm-list"))
        request.user = user

        response = view(request)

        assert response.data == [
            {
                "id": alarm.pk,
                "schedule": "0 8 * * *",
                "active": False,
                "timezone": "UTC",
                "custom_attributes": {},
                "next_firing": "2020-01-02T08:00:00Z",
                "sound": {
                    "id": 1,
                    "name": "buzzer",
                    "audio": f"http://testserver{sound.audio.url}",
                },
                "pre_fire": None,
                "post_fire": None,
            }
        ]
