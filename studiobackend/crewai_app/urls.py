from django.urls import path
from . import views

urlpatterns = [
    path('', views.crewai_view, name='crewai_view'),
]
