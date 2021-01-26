from django.urls import path
from .views.init import *


urlpatterns = [
    path('login/', login),
    path('logout/', logout),

    path('admin/survey/', SurveyAdminListCreate.as_view()),
    path('admin/survey/<str:survey_id>',
         SurveyAdminRetrieveUpdateDestroy.as_view()),

    path('admin/survey/<str:survey_id>/questions/',
         SurveyQuestionsAdminListView.as_view()),

    path('admin/survey/<str:survey_id>/questions/<str:question_id>',
         SurveyQuestionAdminRetrieveUpdateDestroy.as_view()),

    path('survey/', SurveyActiveListView.as_view()),
    path('survey/<str:survey_id>', SurveyDetailView.as_view()),

    path('user/<str:user_id>', UserAnswerDetailView.as_view()),

    path('answer/', AnswerCreateView.as_view()),
]
