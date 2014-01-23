from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
    url(
        r'^u/(?P<pk>\d+)/$',
        login_required(views.UniverseDetailView.as_view()),
        name='udetail',
    ),
    url(
        r'^c/(?P<pk>\d+)/$',
        login_required(views.CharacterDetailView.as_view()),
        name='cdetail',
    ),
    url(
        r'^a/(?P<pk>\d+)/$',
        login_required(views.ArtifactDetailView.as_view()),
        name='adetail',
    ),
    url(
        r'^u/$',
        login_required(views.UniverseListView.as_view()),
        name='ulist',
    ),
    url(
        r'^u/games/$',
        login_required(views.GamesView.as_view()),
        name='glist',
    ),
    url(
        r'^c/$',
        login_required(views.CharacterListView.as_view()),
        name='clist',
    ),
    url(
        r'^a/$',
        login_required(views.ArtifactListView.as_view()),
        name='alist',
    ),
    url(
        r'^$', 
        login_required(TemplateView.as_view(template_name="archive/archive_front.html")),
        name='archive_front',
    ),
)
