from django.contrib import admin
from . import models

admin.site.register(models.Universe)
admin.site.register(models.Character)
admin.site.register(models.ContactPerson)
admin.site.register(models.Artifact)
