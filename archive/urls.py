from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns('',
    url(r'^u/(?P<pk>\d+)/$', views.UniverseDetailView.as_view(), name='udetail'),
    url(r'^c/(?P<pk>\d+)/$', views.CharacterDetailView.as_view(), name='cdetail'),
    url(r'^a/(?P<pk>\d+)/$', views.ArtifactDetailView.as_view(), name='adetail'),
    url(r'^u/$', views.UniverseListView.as_view(), name='ulist'),
    url(r'^u/games/$', views.GamesView.as_view(), name='glist'),
    url(r'^c/$', views.CharacterListView.as_view(), name='clist'),
    url(r'^a/$', views.ArtifactListView.as_view(), name='alist'),
    url(r'^$', TemplateView.as_view(template_name="archive/archive_front.html"), name='archive_front'),
)
