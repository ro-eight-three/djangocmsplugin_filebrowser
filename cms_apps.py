from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class FileBrowserApphook(CMSApp):
    app_name = "filebrowser-restapi"
    name = _("FileBrowser REST API")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["cmsplugin_filebrowser.urls"]


apphook_pool.register(FileBrowserApphook)
