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
        ('キチ度', {'fields': ['para_crazy']}),
        ('アスペ度', {'fields': ['para_aspect']}),
        ('池沼度', {'fields': ['para_intdis']}),
        ('狂気度', {'fields': ['para_madness']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
