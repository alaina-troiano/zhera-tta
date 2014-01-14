from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns('',
    url(r'^events/(?P<pk>\d+)/$', views.EventDetailView.as_view(template_name="community/event_detail.html"), name='event_detail'),
    url(r'^events/$', views.EventListView.as_view(template_name="community/event_list.html"), name='event_list'),
    url(r'^$', TemplateView.as_view(template_name="community/front.html"), name='community_front'),
)
