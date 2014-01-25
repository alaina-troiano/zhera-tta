from django.db import models
from django.contrib.auth.models import User
from archive.models import Universe


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    universe = models.ForeignKey(Universe)
    about = models.TextField()
    contact_number = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return self.user.first_name # the last_name field is not used


class Staff(models.Model):
    user = models.ForeignKey(User)
    
    class Meta:
        verbose_name_plural = 'Staff'


class Webmaster(models.Model):
    user = models.ForeignKey(User)
