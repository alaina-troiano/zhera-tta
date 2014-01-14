from django.db import models
from django.utils import timezone
from cms.models.pluginmodel import CMSPlugin


class Event(models.Model):
    title = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()

    def __unicode__(self):
        return str(self.title)


# This is a plugin model (configuration).
class EventPluginModel(CMSPlugin):
    num_to_show = models.IntegerField()
    
    def get_list(self):
        if (self.num_to_show == 0): # ongoing events
            return Event.objects.filter(start_time__lt=timezone.now()).filter(end_time__gt=timezone.now())
        if (self.num_to_show > 0): # soonest upcoming events
            return Event.objects.filter(start_time__gt=timezone.now()).order_by('start_time')[:self.num_to_show]
        else: # recently ended events
            return Event.objects.filter(end_time__lt=timezone.now()).order_by('-end_time')[:(self.num_to_show * -1)]
    
    def get_type(self):
        if (self.num_to_show == 0):
            return 'ongoing'
        if (self.num_to_show > 0):
            return 'upcoming'
        else:
            return 'recent'
