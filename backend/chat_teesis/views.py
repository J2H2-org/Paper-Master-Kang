# Create your views here.
import json

from django.http import HttpResponse
from requests import request
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from elasticsearch import Elasticsearch
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from django.core import serializers

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


class SearchQtoAViewSet(APIView):
    def get(self, request):
        if request.method == 'GET':
            body = json.loads(request.body)

            return Response(body)
        return Response({"message": "Hello world!"})


class SRViewSet(APIView):  # 엘라스틱서치 학과/주제 전체검색 및 등록

    def get(self, request):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        docs = es.search(index='search_1',
                         body={
                             "query": {
                                 "match_all": {
                                 }
                             }
                         })
        data_list = []
        for data in docs['hits']['hits']:
            data_list.append(data.get('_source'))

        return Response({'data': data_list})

    def post(self, request):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        es.index(index='search_1', body=request.body)
        return HttpResponse(request.body)


class SDViewSet(APIView):  # 엘라스틱서치 학과/주제 검색어로 검색
    def get(self, request, **kwargs):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        search = kwargs['search_word']

        if not search:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})
        docs = es.search(index='search_1',
                         body={
                             "from": 0,
                             "size": 3,
                             "query": {
                                 "multi_match": {
                                     "query": search,
                                     "fields": ["major", "subject"]
                                 },
                             }
                         })
        data_list = []
        for data in docs['hits']['hits']:
            data_list.append(data.get('_source'))

        return Response({'data': data_list})


class SIViewSet(APIView):  # 엘라스틱서치 학과/주제 Id로 검색 및 삭제
    def get(self, request, **kwargs):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        search = kwargs['mentee_question_Id']

        docs = es.search(index='search_1',
                         body={
                             "query": {
                                 "match": {
                                     "mentee_question_Id": search
                                 }
                             }
                         })
        data_list = []
        for data in docs['hits']['hits']:
            data_list.append(data.get('_source'))

        return Response({'data': data_list}, status=200)

    def delete(self, request, **kwargs):  # 멘티아이디로 document 삭제
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        mentee_question_Id = kwargs['mentee_question_Id']
        doc = {"query": {
            "match": {
                "mentee_question_Id": mentee_question_Id,
            }
        }
        }
        docs = es.delete_by_query(index='search_1', doc_type="_doc", body=doc)
        return Response(True)


class SAViewSet(APIView):  # 엘라스틱서치 답변 검색어 검색
    def get(self, request, **kwargs):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        search = kwargs['search_word']

        docs = es.search(index='search_2',
                         body={
                             # "from": 0,
                             # "size": 1,#document 1개만 보이게 하는거
                             "min_score": 3.0,
                             "query": {
                                 "multi_match": {
                                     "query": search,
                                     "fields": ["title", "contents"]
                                 }
                             }
                         })
        data_list = []
        for data in docs['hits']['hits']:
            data_list.append(data.get('_source'))

        return Response({'data': data_list})


class SA2ViewSet(APIView):  # 엘라스틱서치 답변 전체검색 및 등록

    def get(self, request):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        docs = es.search(index='search_2',
                         body={
                             "query": {
                                 "match_all": {
                                 }
                             }
                         })
        data_list = []
        for data in docs['hits']['hits']:
            data_list.append(data.get('_source'))

        return Response({'data': data_list})

    def post(self, request):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        es.index(index='search_2', body=request.body)
        return HttpResponse(request.body)


class MAIViewSet(APIView):  # 질문 아이디로 답변검색

    def get(self, request, **kwargs):
        queryset = mentor_answer_col.objects.all()
        mentee_question_Id = kwargs['mentee_question_Id']

        if mentee_question_Id:
            queryset = queryset.filter(mentee_question_Id__gte=mentee_question_Id)

        data_list = serializers.serialize('json', queryset)
        return HttpResponse(data_list, content_type="text/json-comment-filtered")


class UAViewSet(APIView):  # 유저 아이디로 답변검색

    def get(self, request, **kwargs):
        queryset = mentor_answer_col.objects.all()
        user_Id = kwargs['user_Id']

        if user_Id:
            queryset = queryset.filter(user_Id__gte=user_Id)

        data_list = serializers.serialize('json', queryset)
        return HttpResponse(data_list, content_type="text/json-comment-filtered")


class UQViewSet(APIView):  # 유저 아이디로 질문검색

    def get(self, request, **kwargs):
        queryset = mentee_question_col.objects.all()
        user_Id = kwargs['user_Id']

        if user_Id:
            queryset = queryset.filter(user_Id__gte=user_Id)

        data_list = serializers.serialize('json', queryset)
        return HttpResponse(data_list, content_type="text/json-comment-filtered")

# class GMIViewSet(APIView): #검색된 멘티 아이디 받아서 db로 보내주기
