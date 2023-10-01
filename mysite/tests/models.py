import datetime

from django.db import models
from django.utils import timezone

class Test(models.Model):
    test_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    total_score = models.IntegerField(default=0)
    def __str__(self):
        return self.test_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE,default=0)
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text



class Choice(models.Model):
#    test = models.ForeignKey(Test, on_delete=models.CASCADE,default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
