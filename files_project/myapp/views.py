from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from myapp.models import File
from myapp.serializers import FileSerializer, FileListSerializer


class FilesViewSet(viewsets.ViewSet):
    authentication_classes = []

    @action(detail=False, methods=['post'])
    def upload(self, request):
        serializer = FileSerializer(data=request.FILES)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['get'])
    def files(self, request):
        queryset = File.objects.all()
        return Response(
            FileListSerializer(queryset).data
        )
