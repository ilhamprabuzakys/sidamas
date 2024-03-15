import os
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from sidamas import pagination

from . import serializers
from . import filters
from . import models


class LiterasiViewSet(viewsets.ModelViewSet):
    queryset = models.Literasi.objects.all()
    serializer_class = serializers.LiterasiSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.Page10NumberPagination
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = filters.LiterasiFilter
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.instance
        request_file = self.request.data.get('dokumen', None)
        
        if request_file and instance.dokumen:
            if os.path.isfile(instance.dokumen.path):
                os.remove(instance.dokumen.path)

        serializer.save(updated_by=self.request.user)
        
    def perform_destroy(self, instance):
        if instance.dokumen:
            if os.path.isfile(instance.dokumen.path):
                os.remove(instance.dokumen.path)
        instance.delete()
