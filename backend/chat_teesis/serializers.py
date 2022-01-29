from rest_framework import serializers
from .models import user_col, thesis_plan_col


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_col
        fields = ('user_Id', 'name', 'major', 'degree', 'contact_email', 'belong', 'career', 'img_link')


class TPSerializer(serializers.ModelSerializer):
    class Meta:
        model = thesis_plan_col
        fields = ('thesis_plan_Id', 'subject', 'schedule', 'on_domestic', 'journal_tier', 'purpose', 'user_Id')
