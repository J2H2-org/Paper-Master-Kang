from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import user_col, thesis_plan_col, mentor_answer_col, mentee_question_col, search_col
from .serializers import UserSerializer, TPSerializer, MASerializer, MQSerializer, SearchSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = user_col.objects.all()
    serializer_class = UserSerializer

class TPViewSet(viewsets.ModelViewSet):
    queryset = thesis_plan_col.objects.all()
    serializer_class = TPSerializer

class MAViewSet(viewsets.ModelViewSet):
    queryset = mentor_answer_col.objects.all()
    serializer_class = MASerializer

class MQViewSet(viewsets.ModelViewSet):
    queryset = mentee_question_col.objects.all()
    serializer_class = MQSerializer

class SearchViewSet(viewsets.ModelViewSet):
    queryset = search_col.objects.all()
    serializer_class = SearchSerializer
