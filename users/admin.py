from django.contrib import admin
from .models import UserProfile, Staff, Webmaster

admin.site.register(UserProfile)
admin.site.register(Staff)
admin.site.register(Webmaster)
