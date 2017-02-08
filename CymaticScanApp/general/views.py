from django.views import generic


class TopView(generic.TemplateView):
    template_name = 'top.html'


class QuestionView(generic.TemplateView):
    template_name = 'question.html'
