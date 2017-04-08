__author__ = 'basit'

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # URL to create a TODO
    url(r'^add_todo', views.add_todo_form, name='add_todo'),
    # URL to list all TODOs
    url(r'^list_all', views.todo_list, name='todo_list'),
    # Resolve a TODO
    url(r'^delete', views.resolve, name='resolve'),
]
