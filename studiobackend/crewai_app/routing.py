from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/crewai/$', consumers.CrewAIConsumer.as_asgi()),
]



# from django.urls import re_path
# from . import consumers
#
# websocket_urlpatterns = [
#     re_path(r'ws/crewai/$', consumers.CrewAIConsumer.as_asgi()),
# ]
