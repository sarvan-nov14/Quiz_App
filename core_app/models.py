from django.db import models
from django.contrib.auth.models import User


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Question(TimeStamp):
    """
    Questions belongs to quiz
    """
    question_text = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.question_text


class Quiz(TimeStamp):
    """
    Quiz details
    """
    name = models.CharField(max_length=200)
    question_list = models.ManyToManyField(
        Question, blank=True)

    def __str__(self):
        return self.name


class QuizScore(models.Model):
    """
    To store user quiz scores
    """
    quiz_attended = models.ForeignKey(
        Quiz, related_name='user_quiz', on_delete=models.DO_NOTHING)
    score = models.CharField(max_length=50)


class OptionList(TimeStamp):
    """
    Choices for each question
    """
    choice_text = models.CharField(max_length=200)
    question_text = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True, blank=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text + " " + "|" + " "+str(self.is_correct)


class CustomUser(models.Model):
    """
    Extending core auth User
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quiz_selected = models.ForeignKey(
        QuizScore, related_name='user_quiz_score', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.user.username
