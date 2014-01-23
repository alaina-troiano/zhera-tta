from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from cms.models.pluginmodel import CMSPlugin


# A Manager for retrieving past events
class PastEventManager(models.Manager):
    def get_query_set(self):
        qs = super(PastEventManager, self).get_query_set()
        return qs.filter(end_time__lt=timezone.now()).order_by('-end_time')


# A Manager for retrieving ongoing events
class OngoingEventManager(models.Manager):
    def get_query_set(self):
        qs = super(OngoingEventManager, self).get_query_set()
        return qs.filter(start_time__lt=timezone.now()).filter(end_time__gt=timezone.now()).order_by('start_time')


# A Manager for retrieving future events
class FutureEventManager(models.Manager):
    def get_query_set(self):
        qs = super(FutureEventManager, self).get_query_set()
        return qs.filter(start_time__gt=timezone.now()).order_by('start_time')


# Model for storing information about an event that people may wish to attend.
class Event(models.Model):
    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    
    # This is the default manager; it must be declared first.
    objects = models.Manager()
    # Now for the custom managers.
    past_events = PastEventManager()
    ongoing_events = OngoingEventManager()
    future_events = FutureEventManager()

    # TODO: Compare start/end by date(); if equal, say "Month day, time-time"
    def __unicode__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})


# The model for a plugin that displays some recent or upcoming events.
# Plugin models are used to define configuration information for the plugin.
class EventPluginModel(CMSPlugin):
    num_to_show = models.IntegerField()
    
    def get_list(self):
        if (self.num_to_show == 0): # ongoing events
            return Event.ongoing_events.all()[:self.num_to_show]
        if (self.num_to_show > 0): # soonest upcoming events
            return Event.future_events.all()[:self.num_to_show]
        else: # recently ended events
            return Event.past_events.all()[:(self.num_to_show * -1)]
    
    def get_type(self):
        if (self.num_to_show == 0):
            return 'ongoing'
        if (self.num_to_show > 0):
            return 'upcoming'
        else:
            return 'recent'

