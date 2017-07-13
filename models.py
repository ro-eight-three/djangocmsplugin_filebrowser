from cms.models import CMSPlugin


class FileBrowserPluginModel(CMSPlugin):
    list_path = 'alskdjasldkj'

    def __str__(self):
        return self.list_path


class FileInfo(object):
    def __init__(self, name, is_folder, link):
        self.name = name
        self.is_folder = is_folder
        self.link = link


class ListReply(object):
    def __init__(self, path, fileinfos, parent_path):
        self.path = path
        self.fileinfos = fileinfos
        self.parent_path = parent_path
