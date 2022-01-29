from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import c_answer_col, c_question_col, user_col, thesis_plan_col
from .serializers import CASerializer, CQSerializer, UserSerializer, TPSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = user_col.objects.all()
    serializer_class = UserSerializer


class TPViewSet(viewsets.ModelViewSet):
    queryset = thesis_plan_col.objects.all()
    serializer_class = TPSerializer


class CQViewSet(viewsets.ModelViewSet):
    queryset = c_question_col.objects.all()
    serializer_class = CQSerializer


class CAViewSet(viewsets.ModelViewSet):
    queryset = c_answer_col.objects.all()
    serializer_class = CASerializer
