from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_person/$', views.add_person, name='add_list'),
    url(r'^data/$', views.check_data, name='data_list'),
    url(r'^tasks/$', views.check_task, name='task_list'),
    url(r'^$', views.post_list, name='post_list'),
]