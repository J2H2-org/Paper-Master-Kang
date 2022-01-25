# Create your views here.

from rest_framework import viewsets
from .models import chatphone_items
from .serializers import ChatPhoneSerializer


class ChatPhoneViewSet(viewsets.ModelViewSet):
    queryset = chatphone_items.objects.all()
    serializer_class = ChatPhoneSerializer
