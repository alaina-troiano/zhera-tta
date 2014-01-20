from django.db import models
from django.core.urlresolvers import reverse


# A Manager for retrieving only the game universes
class GameManager(models.Manager):
    def get_query_set(self):
        qs = super(GameManager, self).get_query_set()
        return qs.filter(medium=Universe.GAME).order_by('title')


# Model for information about a universe
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
    
    # This is the default manager; it must be declared first.
    objects = models.Manager()
    # Universe.games will now refer to only the game universes.
    games = GameManager()
    
    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return str(self.title)

    # Returns the associated ContactPerson object
    def _get_contact_person(self):
        mylist = self.contactperson_set.all()
        if (len(mylist) == 0):
            return None
        return mylist[0]
    contact_person = property(_get_contact_person)


# Model for information about a character
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
    
    # Returns the associated ContactPerson object
    # Purpose: ability to display the TTA number on a Character detail page
    def _get_contact_person(self):
        mylist = self.contactperson_set.all()
        if (len(mylist) == 0):
            return None
        return mylist[0]
    contact_person = property(_get_contact_person)


# Connects at most one Character to each Universe, with a couple more details.
class ContactPerson(models.Model):
    universe = models.ForeignKey(Universe, unique=True)
    character = models.ForeignKey(Character)
    lodging = models.BooleanField()
    contact_number = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'contact people'
    
    def __unicode__(self):
        return str(self.character.name)


# Model for items with properties special enough to need archive pages.
class Artifact(models.Model):
    name = models.CharField(max_length=256)
    universe = models.ForeignKey(Universe)
    description = models.TextField()
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return str(self.name)

