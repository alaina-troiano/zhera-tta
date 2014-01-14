from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy, reverse
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from cms.menu_bases import CMSAttachMenu

class ArchiveMenu(CMSAttachMenu):
    name = _("Archive menu")
    
    def get_nodes(self, request):
        nodes = []
        n1 = NavigationNode(_('Universe list'), reverse('ulist'), 1)
        n2 = NavigationNode(_('Character list'), reverse('clist'), 2)
        n3 = NavigationNode(_('Artifact list'), reverse('alist'), 3)
        nodes.append(n1)
        nodes.append(n2)
        nodes.append(n3)
        return nodes

menu_pool.register_menu(ArchiveMenu)
