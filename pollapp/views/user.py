from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from ..models import Survey, Answer
from ..serializers.init import SurveyActiveSerializer, AnswerSerializer, \
    SurveyQuestionsActiveSerializer, CreateAnswerSerializer


class SurveyActiveListView(generics.ListAPIView):
    serializer_class = SurveyActiveSerializer

    def list(self, request, *args, **kwargs):
        serializer = SurveyActiveSerializer(
            Survey.objects.filter(active=True), many=True)
        return Response({
            'data': serializer.data
        })


class SurveyDetailView(generics.RetrieveAPIView):
    serializer_class = SurveyQuestionsActiveSerializer
    lookup_url_kwarg = 'survey_id'

    def retrieve(self, request, *args, **kwargs):
        survey = Survey.objects.filter(id=self.kwargs['survey_id'],
                                       active=True).first()
        result = None
        if survey:
            serializer = SurveyQuestionsActiveSerializer(survey)
            result = serializer.data
        return Response({
            'data': result
        })


class UserAnswerDetailView(generics.RetrieveAPIView):
    serializer_class = AnswerSerializer
    lookup_url_kwarg = 'user_id'

    def retrieve(self, request, *args, **kwargs):
        answer = Answer.objects.filter(user=self.kwargs['user_id'])
        result = None
        if answer:
            serializer = AnswerSerializer(answer, many=True)
            result = serializer.data[1:]
        return Response({
            'data': result
        })


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = CreateAnswerSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
