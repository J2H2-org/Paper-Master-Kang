from rest_framework import serializers
from .models import c_answer_col, c_question_col, user_col, thesis_plan_col


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_col
        fields = ('user_Id', 'name', 'major', 'degree',
                  'contact_email', 'belong', 'career', 'img_link')


class TPSerializer(serializers.ModelSerializer):
    class Meta:
        model = thesis_plan_col
        fields = ('thesis_plan_Id', 'subject', 'schedule',
                  'on_domestic', 'journal_tier', 'purpose', 'user_Id')


class CQSerializer(serializers.ModelSerializer):
    class Meta:
        model = c_question_col
        fields = ('c_question_id', 'c_que', 'que_classification_id')


class CASerializer(serializers.ModelSerializer):
    class Meta:
        model = c_answer_col
        fields = ('c_answer_id', 'c_ans', 'c_question_id')
