from rest_framework import serializers


class FileInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1024)
    is_folder = serializers.BooleanField()
    link = serializers.CharField(max_length=1024)


class ListReplySerializer(serializers.Serializer):
    path = serializers.CharField(max_length=1024)
    fileinfos = FileInfoSerializer(many=True)
    parent_path = serializers.CharField(max_length=1024)
