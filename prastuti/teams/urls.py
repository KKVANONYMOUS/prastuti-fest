from django.urls import path
from .import views

app_name = 'event_registration'

urlpatterns = [
    path('register/<str:event>', views.registerTeam, name='register'),
]