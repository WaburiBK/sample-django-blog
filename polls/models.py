import datetime

from django.db import models
from django.utils import timezone

# A model is the single, definitive source of information about my data
# It contains the essential fields and behaviours of data being stored

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

#field instances tell Django what type of data each field holds
# example: CharField holds character fields, DateTimeField for datetimes
# fields can hold arguments e.g ForeignKey that tells Django that
# each choice is related to a single question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

