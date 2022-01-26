# Create your views here.
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import chatphone_items
from .serializers import ChatPhoneSerializer


class ChatPhoneViewSet(viewsets.ModelViewSet):
    queryset = chatphone_items.objects.all()
    serializer_class = ChatPhoneSerializer

#TODO: 아직 기능은 없음
@api_view(['GET', 'POST', 'DELETE'])
def items_list(request):
    if request.method == 'GET':
        temp = chatphone_items.objects.all()
        temp_ser = ChatPhoneSerializer(chatphone_items, many=True)
        return JsonResponse(temp_ser.data, safe=False)
    elif request.method == 'POST':
        items_data = JSONParser().parse(request)
        temp_ser = ChatPhoneSerializer(data=items_data)
        if temp_ser.is_valid():
            temp_ser.save()
            return JsonResponse(temp_ser.data, status=status.HTTP_201_CREATED)
        return JsonResponse(temp_ser.errors, status=status.HTTP_400_BAD_REQUEST)
