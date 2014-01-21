from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from . import menu

# Allows the archive app and its urls to be attached to a CMS-managed page.
class ArchiveApphook(CMSApp):
    name = _("Archive Apphook")
    urls = ["archive.urls"]
    menus = [menu.ArchiveMenu]

apphook_pool.register(ArchiveApphook)
