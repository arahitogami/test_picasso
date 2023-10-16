import math
import os

from rest_framework import serializers

from app_core import settings
from .models import File


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


class FileSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = (
            'id', 'file', 'file_name', 'size', 'uploaded_at', 'processed'
        )
        write_only = ('file',)

    def get_size(self, obj):
        if os.path.exists(os.path.join(settings.MEDIA_ROOT, obj.file.path)):
            return convert_size(obj.file.size)
        else:
            return "0B"


class FileListSerializer(serializers.ListSerializer):
    child = FileSerializer()
