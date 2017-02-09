from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
       ('title', {'fields': ['title']}),
       ('question', {'fields': ['question']}),
    ]
admin.site.register(Question, QuestionAdmin)
