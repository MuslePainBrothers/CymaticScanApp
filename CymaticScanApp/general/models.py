from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
