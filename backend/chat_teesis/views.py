# Create your views here.
from requests import request
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import user_col, thesis_plan_col, mentor_answer_col, mentee_question_col, c_answer_col, c_question_col, \
    answer_col
from .serializers import UserSerializer, TPSerializer, MASerializer, MQSerializer, CASerializer, CQSerializer, \
    ACSerializer


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


class CQViewSet(viewsets.ModelViewSet):
    queryset = c_question_col.objects.all()
    serializer_class = CQSerializer


class CAViewSet(viewsets.ModelViewSet):
    queryset = c_answer_col.objects.all()
    serializer_class = CASerializer


class ACViewSet(viewsets.ModelViewSet):
    queryset = answer_col.objects.all()
    serializer_class = ACSerializer


@api_view(['GET', 'POST'])
def search_UserViewSet(request, user_Id):
    if request.method == 'GET':
        return Response({"message": "Hello {} world!".format(user_Id)})
    return Response({"message": "Hello world!"})
