# Create your views here.
import json

from django.http import HttpResponse
from requests import request
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import user_col, thesis_plan_col, mentor_answer_col, mentee_question_col, answer_col
from .serializers import UserSerializer, TPSerializer, MASerializer, MQSerializer, ACSerializer


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


class ACViewSet(viewsets.ModelViewSet):
    queryset = answer_col.objects.all()
    serializer_class = ACSerializer


@api_view()
def search_UserViewSet(requests):
    if requests.method == 'GET':
        body = json.loads(requests.body)

        return Response(body)
    return Response({"message": "Hello world!"})
