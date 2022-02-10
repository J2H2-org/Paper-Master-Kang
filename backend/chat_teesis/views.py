# Create your views here.
from requests import request
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from elasticsearch import Elasticsearch
from rest_framework.views import APIView

from .models import user_col, thesis_plan_col, mentor_answer_col, mentee_question_col, c_answer_col, c_question_col, \
    answer_col, search_info_col
from .serializers import UserSerializer, TPSerializer, MASerializer, MQSerializer, CASerializer, CQSerializer, \
    ACSerializer, SDSerializer


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

    def get(self, request, **kwargs):
        es = Elasticsearch(hosts='elasticsearch', port=9200, http_auth=('elastic', 'j2h2'))
        search = kwargs['slug']

        if not search:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})
        if type(search) == int:
            docs = es.search(index='search_data',
                             body={
                                 "query": {
                                     "match": {
                                         "search_info_Id": search
                                     }
                                 }
                             })
            data_list = []
            for data in docs['hits']['hits']:
                data_list.append(data.get('_source'))

            return Response({'data': data_list}, status=200)
        else:
            docs = es.search(index='search_data',
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

        return Response({'data': data_list}, status=200)


class SDViewSet(viewsets.ModelViewSet):
    queryset = search_info_col.objects.all()
    serializer_class = SDSerializer

@api_view(['GET', 'POST'])
def search_UserViewSet(request, user_Id):
    if request.method == 'GET':
        return Response({"message": "Hello {} world!".format(user_Id)})
    return Response({"message": "Hello world!"})
