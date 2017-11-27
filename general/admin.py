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
        ('サイコパス度', {'fields': ['para_psychopath']}),
        ('鬱度', {'fields': ['para_depression']}),
        ('糖質度', {'fields': ['para_schizophrenia']}),
        ('コミュ症度', {'fields': ['para_communication_disorder']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
