from django.views import generic
from .models import Question


class TopView(generic.TemplateView):
    template_name = "top.html"


class QuestionView(generic.TemplateView):
    template_name = "question.html"

    def get_context_data(self, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context['latest_question_list'] = Question.objects.all()
        return context


class ShowQuesListView(generic.TemplateView):
    template_name = "ques_list.html"


class ResultView(generic.TemplateView):
    template_name = "result.html"

