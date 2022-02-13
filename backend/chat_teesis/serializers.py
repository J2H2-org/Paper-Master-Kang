from rest_framework import serializers

from .models import user_col, thesis_plan_col, mentor_answer_col, mentee_question_col


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


class MASerializer(serializers.ModelSerializer):
    class Meta:
        model = mentor_answer_col
        fields = ('mentor_answer_Id', 'mentee_question_Id',
                  'date', 'user_Id', 'title', 'mentor_answer')


class MQSerializer(serializers.ModelSerializer):
    class Meta:
        model = mentee_question_col
        fields = ('user_Id', 'thesis_plan_Id', 'mentee_question_Id',
                  'title', 'date', 'mentee_question')