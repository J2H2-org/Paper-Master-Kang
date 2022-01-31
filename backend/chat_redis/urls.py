from django.urls import path
from .views import my_view

app_name = "chat_redis"

urlpatterns = [
    path('', my_view),
]
