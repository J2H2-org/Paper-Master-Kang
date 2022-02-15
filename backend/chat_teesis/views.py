# Create your views here.
import json

from django.core import serializers
from django.http import HttpResponse
from elasticsearch import Elasticsearch
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
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


class SearchQtoAViewSet(APIView):
    def get(self, request):
        if request.method == 'GET':
            body = json.loads(request.body)

            return Response(body)
        return Response({"message": "Hello world!"})


class SRViewSet(APIView):  # 엘라스틱서치 플랜 전체검색 및 등록

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

        return Response(data_list, status=200)

    def post(self, request):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        es.index(index='search_1', body=request.body)
        return HttpResponse(request.body)


class SDViewSet(APIView):  # 엘라스틱서치 플랜 검색어로 검색한 후 질문아이디만 받아서 질문검색
    def get(self, request):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        search = json.loads(request.body)
        search = search['word']

        if not search:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})
        docs = es.search(index='search_1',
                         body={
                             "from": 0,
                             "size": 3,
                             "_source": ["mentee_question_Id"],  # 검색결과에서 특정필드값만 보이게 하기
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

        queryset = mentee_question_col.objects.all()
        question_list = []
        for i in range(len(data_list)):
            data = (data_list[i]['mentee_question_Id'])

            mentee_query = queryset.filter(mentee_question_Id__exact=data)

            for j in json.loads(serializers.serialize('json', mentee_query)):
                question_list.append(j)
        return HttpResponse(json.dumps(question_list), content_type="text/json-comment-filtered")


class SIViewSet(APIView):  # 엘라스틱서치 플랜 Id로 검색 및 삭제
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

        return Response(data_list, status=200)

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
    def get(self, request):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        search = json.loads(request.body)
        search = search['word']

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

        return Response(data_list, status=200)


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

        return Response(data_list, status=200)

    def post(self, request):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        es.index(index='search_2', body=request.body)
        return HttpResponse(request.body)


class MAIViewSet(APIView):  # 질문 아이디로 답변검색

    def get(self, request, **kwargs):
        queryset = mentor_answer_col.objects.all()
        mentee_question_Id = kwargs['mentee_question_Id']

        if mentee_question_Id:
            queryset = queryset.filter(mentee_question_Id__exact=mentee_question_Id)

        data_list = serializers.serialize('json', queryset)
        return HttpResponse(data_list, content_type="text/json-comment-filtered")


class UAViewSet(APIView):  # 유저 아이디로 답변검색

    def get(self, request, **kwargs):
        queryset = mentor_answer_col.objects.all()
        user_Id = kwargs['user_Id']

        if user_Id:
            queryset = queryset.filter(user_Id__exact=user_Id)

        data_list = serializers.serialize('json', queryset)
        return HttpResponse(data_list, content_type="text/json-comment-filtered")


class UQViewSet(APIView):  # 유저 아이디로 질문검색

    def get(self, request, **kwargs):
        queryset = mentee_question_col.objects.all()
        user_Id = kwargs['user_Id']

        if user_Id:
            queryset = queryset.filter(user_Id__exact=user_Id)

        data_list = serializers.serialize('json', queryset)
        return HttpResponse(data_list, content_type="text/json-comment-filtered")


class UPViewSet(APIView):  # 유저 아이디로 논문계획 검색

    def get(self, request, **kwargs):
        queryset = thesis_plan_col.objects.all()
        user_Id = kwargs['user_Id']

        if user_Id:
            queryset = queryset.filter(user_Id__exact=user_Id)

        data_list = serializers.serialize('json', queryset)
        return HttpResponse(data_list, content_type="text/json-comment-filtered")


class PIQViewSet(APIView):  # 플랜 아이디로 질문 검색

    def get(self, request, **kwargs):
        queryset = mentee_question_col.objects.all()
        thesis_plan_Id = kwargs['thesis_plan_Id']

        if thesis_plan_Id:
            queryset = queryset.filter(thesis_plan_Id__exact=thesis_plan_Id)

        data_list = serializers.serialize('json', queryset)
        return HttpResponse(data_list, content_type="text/json-comment-filtered")
