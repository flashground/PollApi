from ..models import Survey, Question
from rest_framework import serializers


class SurveyCreateAdminSerializer(serializers.ModelSerializer):
    survey_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Survey
        fields = [
            'survey_id', 'title', 'description', 'active',
            'start_date', 'finish_date', 'created_date'
        ]
        read_only_fields = ['survey_id', 'created_date']


class SurveyUpdateAdminSerializer(serializers.ModelSerializer):
    survey_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Survey
        fields = [
            'survey_id', 'title', 'description', 'active',
            'start_date', 'finish_date', 'created_date'
        ]
        read_only_fields = ['survey_id', 'start_date', 'created_date']


class QuestionCreateAdminSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='id', required=False, read_only=True)
    question = serializers.CharField(source='text', required=False)

    class Meta:
        model = Question
        fields = [
            'survey', 'question_id', 'question', 'type',
            'choices', 'active', 'updated_date', 'created_date'
        ]
        read_only_fields = ['start_date', 'created_date']


class SurveyQuestionAdminSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='id', required=False)

    class Meta:
        model = Question
        fields = [
            'question_id', 'type', 'text', 'type',
            'choices', 'active', 'created_date'
        ]
        read_only_fields = ['question_id', 'created_date']