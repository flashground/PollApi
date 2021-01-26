from ..models import Survey, Question, Answer
from rest_framework import serializers


class SurveyActiveSerializer(serializers.ModelSerializer):
    survey_id = serializers.IntegerField(source='id')

    class Meta:
        model = Survey
        fields = [
            'survey_id', 'title', 'description',
            'start_date', 'finish_date'
        ]


class FilterActiveListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(active=True)
        return super(FilterActiveListSerializer, self).to_representation(data)


class QuestionActiveSerializer(serializers.ModelSerializer):
    question_id = serializers.IntegerField(source='id')

    class Meta:
        model = Question
        fields = ['question_id', 'type', 'text', 'type', 'choices']
        list_serializer_class = FilterActiveListSerializer


class SurveyQuestionsActiveSerializer(serializers.ModelSerializer):
    survey_id = serializers.IntegerField(source='id')
    questions = QuestionActiveSerializer(many=True, source='question_set')

    class Meta:
        model = Survey
        fields = [
            'survey_id', 'title', 'description',
            'start_date', 'finish_date', 'questions'
        ]


class AnswerSerializer(serializers.ModelSerializer):

    survey_id = serializers.IntegerField(source='question.survey_id')
    survey_name = serializers.CharField(source='question.survey')
    answer_id = serializers.IntegerField(source='id')
    answer_text = serializers.CharField(source='text')
    question_id = serializers.IntegerField(source='question.id')
    question_text = serializers.CharField(source='question.text')

    class Meta:
        model = Answer
        fields = ['survey_id', 'survey_name',
                  'question_id', 'question_text',
                  'answer_id', 'answer_text', 'created_date']


class CreateAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['user', 'question', 'text']
