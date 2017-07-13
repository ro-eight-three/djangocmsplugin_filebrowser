from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from .models import FileBrowserPluginModel


class FileBrowserPluginPublisher(CMSPluginBase):
    model = FileBrowserPluginModel
    module = _("FileBrowser")
    name = _("FileBrowser Plugin")
    render_template = "cmsplugin_filebrowser/plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(FileBrowserPluginPublisher)
