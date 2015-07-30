from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.SolutionView.as_view(), name='solution'),
    url(r'^(?P<pk>([0-9]|[A-Z])+)/$', views.EventView.as_view(), name='event'),
    url(r'^search_form/$', views.SearchView.as_view(), name='search_form'),
    url(r'^results/$', views.ResultsView.as_view(), name='results'),
    url(r'^search/$', views.search, name='search'),
    url(r'^generate_txt/(?P<results>[0-9]+(_[0-9]+)*)/$', views.generate_txt, name="generate_txt"),
    url(r'^generate_targz/(?P<results>[0-9]+(_[0-9]+)*)/$', views.generate_targz, name="generate_targz"),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.my_logout, name='my_logout'),
]
