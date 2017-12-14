from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^person_for_picket/$', views.set_person_for_picket, name='person_for_picket'),
    url(r'^task_complete/$', views.task_complete, name='task_complete'),

    url(r'^about_person/$', views.about_person, name='about_person'),

    url(r'^add_person/$', views.add_person, name='add_list'),
    url(r'^all_person/$', views.all_person, name='all_person_list'),
    url(r'^tasks/$', views.check_task, name='task_list'),

    url(r'^$', views.post_list, name='post_list'),
]