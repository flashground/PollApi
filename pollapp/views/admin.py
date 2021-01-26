from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response

from ..authentication import JWTAuthentication
from ..models import Survey, Question
from ..serializers.init import SurveyQuestionAdminSerializer, \
    SurveyCreateAdminSerializer, SurveyUpdateAdminSerializer, \
    QuestionCreateAdminSerializer


class SurveyAdminListCreate(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def list(self, request, *args, **kwargs):
        serializer = SurveyCreateAdminSerializer(
            Survey.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = SurveyCreateAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


class SurveyAdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'survey_id'

    def retrieve(self, request, *args, **kwargs):
        survey = get_object_or_404(Survey, id=self.kwargs['survey_id'])
        serializer = SurveyUpdateAdminSerializer(survey)
        return Response({
            'data': serializer.data
        })

    def update(self, request, *args, **kwargs):
        survey = Survey.objects.get(id=self.kwargs['survey_id'])
        serializer = SurveyUpdateAdminSerializer(instance=survey, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        survey = get_object_or_404(Survey, id=self.kwargs['survey_id'])
        survey.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SurveyQuestionsAdminListView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'survey_id'

    def list(self, request, *args, **kwargs):
        serializer = SurveyQuestionAdminSerializer(
            Question.objects.filter(survey=self.kwargs['survey_id']),
            many=True)
        return Response({
            'data': serializer.data
        })

    def create(self, request, *args, **kwargs):
        request.data['survey'] = kwargs['survey_id']
        serializer = QuestionCreateAdminSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


class SurveyQuestionAdminRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    lookup_url_kwarg = 'question_id'

    def retrieve(self, request, *args, **kwargs):
        # question = Question.objects.get(id=self.kwargs['question_id'])
        question = get_object_or_404(Question, id=self.kwargs['question_id'])
        serializer = QuestionCreateAdminSerializer(question)
        return Response({
            'data': serializer.data
        })

    def update(self, request, *args, **kwargs):
        request.data['survey'] = kwargs['survey_id']
        question = get_object_or_404(Question, id=self.kwargs['question_id'])
        serializer = QuestionCreateAdminSerializer(instance=question, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, *args, **kwargs):
        question = get_object_or_404(Question, id=self.kwargs['question_id'])
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
