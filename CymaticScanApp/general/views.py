from django.views import generic
from .models import Question, Answer


class TopView(generic.TemplateView):
    template_name = "top.html"


class QuestionView(generic.TemplateView):
    template_name = "question.html"

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionView, self).get_context_data(**kwargs)
        context["questions"] = Question.objects.all()
        context["count"] = 0
        return context


class ResultView(generic.TemplateView):
    template_name = "result.html"

    def post(self, request, *args, **kwargs):
        ques = Question.objects.order_by("id")

        # ユーザの解答
        list_your_answer = []
        for i in range(0, len(ques)):
            list_your_answer.append(Answer.objects.get(pk=self.request.POST["answer"+str(i+1)]))

        # パラメータ計算（サンプル）
        for ans in list_your_answer:
            print(ans, ans.para_A, ans.para_B, ans.para_C)

        # デバッグ用
        ques_your_answer = zip(ques, list_your_answer)

        context = self.get_context_data(**kwargs)
        context["list_your_answer"] = list_your_answer
        context["ques_your_answer"] = ques_your_answer

        return self.render_to_response(context)
