from django.core.exceptions import ValidationError
from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=100, null=True)
    start_date = models.DateTimeField(null=True)
    finish_date = models.DateTimeField(null=True)
    description = models.TextField(max_length=300, null=True)
    active = models.BooleanField(default=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def validate_choices(choices):
    """
    Проверка соответствия заполненой строки с вариантами ответа и типом вопроса
    :param String choices: The string representing the user choices.
    """
    values = choices.split(',')
    empty = 0
    for value in values:
        if value.replace(" ", "") == "":
            empty += 1
    if len(values) < 2 + empty:
        msg = "The selected field requires an associated list of choices."
        msg += " Choices must contain more than one item."
        raise ValidationError(msg)


class Question(models.Model):
    TEXT = "text"
    SELECT = "select"
    SELECT_MULTIPLE = "select-multiple"

    QUESTION_TYPES = (
        (TEXT, "text (multiple line)"),
        (SELECT, "select"),
        (SELECT_MULTIPLE, "Select Multiple"),
    )

    survey = models.ForeignKey('Survey', on_delete=models.DO_NOTHING, null=True)
    type = models.CharField(max_length=200,
                            choices=QUESTION_TYPES,
                            default=TEXT)
    text = models.CharField(max_length=4096, null=True)
    choices = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.type in [Question.SELECT, Question.SELECT_MULTIPLE]:
            validate_choices(self.choices)
        super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.text


class Answer(models.Model):
    user = models.IntegerField()
    question = models.ForeignKey(Question,
                                 on_delete=models.DO_NOTHING,
                                 related_name='answer')
    text = models.TextField(max_length=4096)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'question']

    def __str__(self):
        return f"{self.user} {self.question.text}"
