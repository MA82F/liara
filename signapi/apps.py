from django.apps import AppConfig
from rest_framework.decorators import api_view
from rest_framework.response import Response

class SignapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signapi'
