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

        total_score = [0, 0, 0, 0]
        score_name = ["キチ度", "アスペ度", "池沼度", "狂気度"]

        # パラメータ計算（サンプル）
        for ans in list_your_answer:
            total_score[0] += ans.para_crazy
            total_score[1] += ans.para_aspect
            total_score[2] += ans.para_intdis
            total_score[3] += ans.para_madness

        # デバッグ用
        ques_your_answer = zip(ques, list_your_answer)
        score_name_total_score = zip(score_name, total_score)

        # 結果のテキスト
        if total_score[0] > 4:
            result_text = "軽度のキチ"
        elif total_score[1] > 5:
            result_text = "軽度のアスペ"
        elif total_score[2] > 3:
            result_text = "どこにでもいる池沼"
        elif total_score[3] > 6:
            result_text = "かなりやばいやつ"
        else:
            result_text = "ふつうの人"

        context = self.get_context_data(**kwargs)
        context["list_your_answer"] = list_your_answer
        context["ques_your_answer"] = ques_your_answer
        context["score_name_total_score"] = score_name_total_score
        context["result_text"] = result_text
        context["para_A"] = total_score[0]
        context["para_B"] = total_score[1]
        context["para_C"] = total_score[2]
        context["para_D"] = total_score[3]


        return self.render_to_response(context)
