# urls.py

from django.urls import path

from .views import my_view

app_name = "redistest"

urlpatterns = [  
    path('', my_view),
]