from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from models import EventPluginModel


# A view for a plugin that displays some recent or upcoming events.
class EventPlugin(CMSPluginBase):
    model = EventPluginModel
    name = _("Events list")
    render_template = "event_plugin.html"
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(EventPlugin)
