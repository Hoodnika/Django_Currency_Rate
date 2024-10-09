from django.urls import path

from main_app.apps import MainAppConfig
from main_app.views import get_current_usd

app_name = MainAppConfig.name

urlpatterns = [
    path('get_current_usd/', get_current_usd, name='get_current_usd'),
]