from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/login/', 
        'django.contrib.auth.views.login',
        name="login"),
    url(r'^accounts/logout/', 
        'django.contrib.auth.views.logout', 
        name="logout"),
    url(r'^', include('cms.urls')),
)

# Copied from the CMS tutorial; not sure what it does.
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
