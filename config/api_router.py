from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from alarms.views import AlarmViewSet, SoundViewSet
from clock.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("alarms", AlarmViewSet)
router.register("sounds", SoundViewSet)


app_name = "api"
urlpatterns = router.urls
