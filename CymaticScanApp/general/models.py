from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=200)
    para_crazy = models.IntegerField()
    para_aspect = models.IntegerField()
    para_psychopath = models.IntegerField()
    para_depression = models.IntegerField()
    para_schizophrenia = models.IntegerField()
    para_communication_disorder = models.IntegerField()

    def __str__(self):
        return self.text


class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    answer = models.ManyToManyField(Answer, verbose_name="list of answer")

    def __str__(self):
        return self.title
