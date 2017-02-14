from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('質問タイトル', {'fields': ['title']}),
        ('内容', {'fields': ['text']}),
        ('答え', {'fields': ['answer']}),
    ]


class AnswerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('答え', {'fields': ['text']}),
        ('パラメータA', {'fields': ['para_A']}),
        ('パラメータB', {'fields': ['para_B']}),
        ('パラメータC', {'fields': ['para_C']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
