from django.db import models
from django.core.urlresolvers import reverse

# Define Manager classes before their models

class Universe(models.Model):
    BOOK = 'Book'
    COMIC = 'Graphic novel'
    LIVE_ACTION = 'Live-action'
    ANIMATION = 'Animation'
    AUDIO = 'Audio-only'
    GAME = 'Game'
    MEDIUM_CHOICES = (
        (BOOK, 'Book'),
        (COMIC, 'Graphic novel'),
        (LIVE_ACTION, 'Live-action'),
        (ANIMATION, 'Animation'),
        (AUDIO, 'Audio-only'),
        (GAME, 'Game'),
    )

    title = models.CharField("title of work", max_length=256)
    medium = models.CharField(max_length=16, choices=MEDIUM_CHOICES, default=BOOK)
    time_difference = models.CharField(max_length=256)
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name="parent universe")
    description = models.TextField()
    
    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return str(self.title)

    #def get_absolute_url(self):
    #    return reverse('zverse:udetail', kwargs={'pk': self.pk})

    # contactperson_set has only one object in it, return that
    def _get_contact_person(self):
        mylist = self.contactperson_set.all()
        if (len(mylist) == 0):
            return None
        return mylist[0]
    contact_person = property(_get_contact_person)


class Character(models.Model):
    name = models.CharField(max_length=256)
    home = models.ForeignKey(Universe, verbose_name="universe of origin")
    species = models.CharField(max_length=256, default='Human')
    language = models.CharField("native language", max_length=256, default='English')
    description = models.TextField("biographical information")

    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return str(self.name)

    #def get_absolute_url(self):
    #    return reverse('zverse:cdetail', kwargs={'pk': self.pk})
    
    # contactperson_set has only one object in it, return that
    def _get_contact_person(self):
        mylist = self.contactperson_set.all()
        if (len(mylist) == 0):
            return None
        return mylist[0]
    contact_person = property(_get_contact_person)


class ContactPerson(models.Model):
    universe = models.ForeignKey(Universe, unique=True)
    character = models.ForeignKey(Character)
    lodging = models.BooleanField()
    contact_number = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'contact people'
    
    def __unicode__(self):
        return str(self.character.name)


class Artifact(models.Model):
    name = models.CharField(max_length=256)
    universe = models.ForeignKey(Universe)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return str(self.name)

