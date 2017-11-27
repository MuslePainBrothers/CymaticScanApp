from django.conf.urls import url
from . import views

app_name = "general"
urlpatterns = [
    url(r'^$', views.TopView.as_view(), name='top'),
    url(r'^question/$', views.QuestionView.as_view(), name='question'),
    url(r'^result/$', views.ResultView.as_view(), name='result'),
]
