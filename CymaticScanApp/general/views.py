from django.views import generic


class TopView(generic.TemplateView):
    template_name = "top.html"


class QuestionView(generic.TemplateView):
    template_name = "question.html"


class ShowQuesListView(generic.TemplateView):
    template_name = "ques_list.html"


class ResultView(generic.TemplateView):
    template_name = "result.html"

