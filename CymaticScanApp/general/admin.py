from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
       ('title', {'fields': ['title']}),
       ('text', {'fields': ['text']}),
    ]


class AnswerAdmin(admin.ModelAdmin):
    fieldsets = [
       ('question', {'fields': ['question']}),
       ('text', {'fields': ['text']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
