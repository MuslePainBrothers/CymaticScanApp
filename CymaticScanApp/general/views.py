from django.http import HttpResponse
from django.views import generic
from .models import Question, Answer
from django.shortcuts import render_to_response, redirect


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
            try:
                list_your_answer.append(Answer.objects.get(pk=self.request.POST["answer"+str(i+1)]))
            except:
                return redirect("general:question")

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

        max= 0
        for i in range(0, 3):
            if max < total_score[i]:
                max = total_score[i]

        # 結果のテキスト
        if total_score[0] == max:
            result_text = "基地外タイプ"
        elif total_score[1] == max:
            result_text = "アスペタイプ"
        elif total_score[2] == max:
            result_text = "いけ沼タイプ"
        elif total_score[3] == max:
            result_text = "サイコパスタイプ"
        else:
            result_text = "ふつうの人"

        context = self.get_context_data(**kwargs)
        context["list_your_answer"] = list_your_answer
        context["ques_your_answer"] = ques_your_answer
        context["score_name_total_score"] = score_name_total_score
        context["result_text"] = result_text
        context["crazy"] = total_score[0]
        context["aspect"] = total_score[1]
        context["intdis"] = total_score[2]
        context["madness"] = total_score[3]


        return self.render_to_response(context)

