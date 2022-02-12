# Create your views here.
from requests import request
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from elasticsearch import Elasticsearch
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse

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


class SRViewSet(APIView):

    def get(self,request):
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

        return Response({'data': data_list}, status=200)

    def post(self, request):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        es.index(index='search_1', body=request.body)
        return HttpResponse(request.body)


class SDViewSet(APIView):
    def get(self, request, **kwargs):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        search = kwargs['slug']

        if not search:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})
        docs = es.search(index='search_1',
                            body={
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

        return Response({'data': data_list},status=200)

    def delete(self, request, **kwargs):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        mentee_question_Id = kwargs['slug']
        doc = {"query": {
            "match": {
                "mentee_question_Id": mentee_question_Id,
            }
        }
        }
        docs = es.delete_by_query(index='search_1', doc_type="_doc", body=doc)
        data_list = []
        for data in docs:
            data_list.append(data)
        # .get('_source')
        return Response(data_list)

    # def put(self,request,**kwargs):
    #     es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
    #     update = kwargs['slug']
    #     doc = {"query": {
    #         "match": {
    #             "mentee_question_Id": update
    #         }
    #     }
    #     }
    #     docs = es.update_by_query(index='search_1', doc_type="_doc", body=)


class SIViewSet(APIView):
    def get(self,request,**kwargs):

        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        search = kwargs['slug']

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

        return Response({'data': data_list})

@api_view(['GET', 'POST'])
def search_UserViewSet(request, user_Id):
    if request.method == 'GET':
        return Response({"message": "Hello {} world!".format(user_Id)})
    return Response({"message": "Hello world!"})
