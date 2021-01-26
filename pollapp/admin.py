from django.contrib import admin
from pollapp.models import Survey,Question,Answer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass