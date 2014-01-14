from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from .models import *

class EventListView(ListView):
    template_name = "community/event_list.html"
    model = Event


class EventDetailView(DetailView):
    model = Event
