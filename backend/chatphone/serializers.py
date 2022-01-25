from rest_framework import serializers
from .models import chatphone_items


class ChatPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = chatphone_items
        fields = ('id', 'names', 'color')
