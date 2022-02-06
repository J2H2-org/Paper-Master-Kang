from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from elasticsearch import Elasticsearch
from rest_framework.views import APIView

from .models import user_col, thesis_plan_col, mentor_answer_col, mentee_question_col
from .serializers import UserSerializer, TPSerializer, MASerializer, MQSerializer


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

# class SearchViewSet(viewsets.ModelViewSet):
#     queryset = search_info_col.objects.all()
#     serializer_class = SearchSerializer

class SRViewSet(APIView):
    serializer_class = None
    queryset = None
    def get(self, request):
        es = Elasticsearch([{'host':'localhost','port':'9200'}])

        search_word = request.query_params.get('search')

        if not search_word:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'message':'search word param is missing'})

        docs = es.search(index='search',
                         doc_type='_doc',
                         body={
                             "query":{
                                 "multi_match":{
                                     "query": search_word,
                                     "fields":["major","subject","tag"]
                                 },
                             }
                         })
        data_list = []
        for data in docs['hits']['hits']:
            data_list.append(data.get('_source'))

        return Response(data_list)



