""" urls for todolist """
from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'todos.views.user_login'),
    url(r'^emailing/$', 'todos.views.email_todo'),
    url(r'^deletetodo/$', 'todos.views.delete_todo'),
    url(r'^home.html/$','todos.views.index'),
    url(r'^base.html/$','todos.views.index'),
    url(r'^login/$' ,'todos.views.user_login'),
    url(r'^base/$', 'todos.views.logout_view'),
    url(r'^addtodo/$', 'todos.views.addtodo_form'),
    url(r'^accounts/profile/$','todos.views.index'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
