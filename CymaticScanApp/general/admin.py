from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
       ('title', {'fields': ['title']}),
       ('question_text', {'fields': ['question_text']}),
    ]
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
