from django.urls import path

from .views.init import *

urlpatterns = [
    path('admin/survey/', SurveyAdminListCreate.as_view()),
    path('admin/survey/<str:survey_id>',
         SurveyAdminRetrieveUpdateDestroy.as_view()),

    path('admin/survey/<str:survey_id>/questions/',
         SurveyQuestionsAdminListView.as_view()),

    path('admin/survey/<str:survey_id>/questions/<str:question_id>',
         SurveyQuestionAdminRetrieveUpdateDestroy.as_view()),
    ]
