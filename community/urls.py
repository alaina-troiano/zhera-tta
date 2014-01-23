from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('',
    url(
        r'^events/(?P<pk>\d+)/$',
        login_required(views.EventDetailView.as_view()),
        name='event_detail',
    ),
    url(
        r'^events/$',
        login_required(views.EventListView.as_view()),
        name='event_list',
    ),
    url(
        r'^$',
        login_required(TemplateView.as_view(template_name="community/front.html")),
        name='community_front',
    ),
)
