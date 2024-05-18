import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import crewai_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studiobackend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            crewai_app.routing.websocket_urlpatterns
        )
    ),
})


# import os
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import crewai_app.routing
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studiobackend.settings')
#
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             crewai_app.routing.websocket_urlpatterns
#         )
#     ),
# })
