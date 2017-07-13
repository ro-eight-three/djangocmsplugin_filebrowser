import os
from django.core.urlresolvers import reverse
from rest_framework import views, status
from rest_framework.response import Response
from .models import FileInfo, ListReply
from .serializers import ListReplySerializer


class ListPathView(views.APIView):
    def get(self, request, *args, **kwargs):
        path = os.path.join('/', kwargs['path'])
        listreply = ListReply(path,
                              list_folder(path),
                              full_link(os.path.dirname(path)))
        serializer = ListReplySerializer(listreply)
        return Response(serializer.data, status=status.HTTP_200_OK)


def full_link(path):
    return reverse('filebrowser-restapi:list', kwargs={'path': path})


def list_folder(path):
    """
    get the contents of path, subdirecotries first
    """
    fileinfos = []

    for de in os.scandir(path):
        fileinfo = FileInfo(de.name, de.is_dir(), full_link(de.path))
        fileinfos.append(fileinfo)

    return fileinfos
