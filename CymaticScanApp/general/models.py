from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=30)
    question = models.TextField(max_length=200)
