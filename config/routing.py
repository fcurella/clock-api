from channels.routing import ProtocolTypeRouter, URLRouter
import alarms.routing

application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
        "websocket": URLRouter(alarms.routing.websocket_urlpatterns),
    }
)
