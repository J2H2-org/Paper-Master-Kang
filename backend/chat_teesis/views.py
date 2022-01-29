from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import user_col, thesis_plan_col
from .serializers import UserSerializer, TPSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = user_col.objects.all()
    serializer_class = UserSerializer


class TPViewSet(viewsets.ModelViewSet):
    queryset = thesis_plan_col.objects.all()
    serializer_class = TPSerializer
