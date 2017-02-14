from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=200)
    para_A = models.IntegerField()
    para_B = models.IntegerField()
    para_C = models.IntegerField()

    def __str__(self):
        return self.text


class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    answer = models.ManyToManyField(Answer, verbose_name="list of answer")

    def __str__(self):
        return self.title
