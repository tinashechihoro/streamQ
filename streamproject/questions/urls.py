from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /questions/
    url(r'^$', views.index, name='index'),
    # ex: /questions/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /questions/5/results/
    url(r'^(?P<question_id>[0-9]+)/update/$', views.update, name='update'),
    # ex: /questions/5/comment/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.comment, name='comment'),
]