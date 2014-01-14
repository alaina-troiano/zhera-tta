from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy, reverse

from models import *

class UniverseListView(ListView):
    template_name = "archive/universe_list.html"
    model = Universe
    context_object_name = 'universe_list'


class CharacterListView(ListView):
    template_name = "archive/character_list.html"
    model = Character
    context_object_name = 'character_list'


class ArtifactListView(ListView):
    template_name = "archive/artifact_list.html"
    model = Artifact
    context_object_name = 'artifact_list'


class UniverseDetailView(DetailView):
    model = Universe
    template_name = "archive/universe_detail.html"


class CharacterDetailView(DetailView):
    model = Character
    template_name = "archive/character_detail.html"


class ArtifactDetailView(DetailView):
    model = Artifact
    template_name = "archive/artifact_detail.html"
