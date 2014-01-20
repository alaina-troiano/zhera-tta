from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy, reverse

from models import Universe, Character, Artifact

# Universe
class UniverseListView(ListView):
    template_name = "archive/universe_list.html"
    model = Universe
    context_object_name = 'universe_list'


class GamesView(TemplateView):
    template_name = "archive/games_list.html"
    
    def get_context_data(self, **kwargs):
		context = super(GamesView, self).get_context_data(**kwargs)
		context['games'] = Universe.games
		return context


class UniverseDetailView(DetailView):
    model = Universe
    template_name = "archive/universe_detail.html"


# Character
class CharacterListView(ListView):
    template_name = "archive/character_list.html"
    model = Character
    context_object_name = 'character_list'


class CharacterDetailView(DetailView):
    model = Character
    template_name = "archive/character_detail.html"


# Artifact
class ArtifactListView(ListView):
    template_name = "archive/artifact_list.html"
    model = Artifact
    context_object_name = 'artifact_list'


class ArtifactDetailView(DetailView):
    model = Artifact
    template_name = "archive/artifact_detail.html"
