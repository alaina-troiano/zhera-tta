from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu
from .models import Event


# Adds lists and objects from the community app to the CMS's auto-generated
# menu so that they will show up in the breadcrumbs in intuitive ways.
class CommunityMenu(CMSAttachMenu):
    name = _("Community menu")
    
    def get_nodes(self, request):
        nodes = []
        n1 = NavigationNode(_('Event list'), reverse('event_list'), 1)
        nodes.append(n1)
        for event in Event.objects.all():
            node = NavigationNode(
                event.title,
                event.get_absolute_url(),
                (event.pk + 1),
                1)
            nodes.append(node)
        return nodes

menu_pool.register_menu(CommunityMenu)
