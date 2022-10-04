from django.db import models

# Create your models here.
class Question(models.Model):  # table 1
    question_text = models.CharField(max_length=200)  # field 1
    pub_date = models.DateTimeField('date published')  # field 2

class Choice(models.Model):  # table 2
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # filed 1
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)