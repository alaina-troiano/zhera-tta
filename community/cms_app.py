from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

# Allows the community app and its urls to be attached to a CMS-managed page.
class CommunityApphook(CMSApp):
    name = _("Community Apphook")
    urls = ["community.urls"]

apphook_pool.register(CommunityApphook)
