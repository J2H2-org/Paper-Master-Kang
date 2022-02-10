# Create your views here.
import json

from django.http import HttpResponse
from requests import request
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from elasticsearch import Elasticsearch
from rest_framework.views import APIView


from .models import user_col, thesis_plan_col, mentor_answer_col, mentee_question_col, answer_col, search_info_col
from .serializers import UserSerializer, TPSerializer, MASerializer, MQSerializer, ACSerializer, SDSerializer


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


@api_view(['GET', 'POST'])
def search_UserViewSet(requests):
    if requests.method == 'GET':
        body = json.loads(requests.body)

        return Response(body)
    return Response({"message": "Hello world!"})

  
class CAViewSet(viewsets.ModelViewSet):
    queryset = c_answer_col.objects.all()
    serializer_class = CASerializer


class SRViewSet(APIView):

    def get(self, request, **kwargs):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        search = kwargs['slug']

        if not search:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})
        if type(search) == int:
            docs = es.search(index='teesis.chat_teesis_search_info_col',
                             body={
                                 "query": {
                                     "match": {
                                         "user_Id": search
                                     }
                                 }
                             })
            data_list = []
            for data in docs['hits']['hits']:
                data_list.append(data.get('_source'))

            return Response({'data': data_list}, status=200)
        else:
            docs = es.search(index='teesis.chat_teesis_search_info_col',
                             body={
                                 "query": {
                                     "multi_match": {
                                         "query": search,
                                         "fields": ["major", "subject", "tag"]
                                     },
                                 }
                             })
        data_list = []
        for data in docs['hits']['hits']:
            data_list.append(data.get('_source'))

        return Response({'data': data_list}, status=200)


class SDViewSet(viewsets.ModelViewSet):
    queryset = search_info_col.objects.all()
    serializer_class = SDSerializer
