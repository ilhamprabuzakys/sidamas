from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from sidamas import pagination

from kegiatan import models
from kegiatan.api import serializers
from kegiatan.api import filters

# class DAYATIF_BINAAN_TEKNIS_ViewSet(viewsets.ModelViewSet):
#     queryset = models.DAYATIF_BINAAN_TEKNIS.objects.all()
#     serializer_class = serializers.DAYATIF_BINAAN_TEKNIS_Serializer
#     permission_classes = [permissions.IsAuthenticated]
#     pagination_class = pagination.Page10NumberPagination
#     filter_backends = [DjangoFilterBackend, ]
#     filterset_class = filters.DAYATIF_BINAAN_TEKNIS_Filters
    
#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)

#     def perform_update(self, serializer):
#         serializer.save(updated_by=self.request.user)
        
#     def get_view_name(self):
#         return "DAYATIF BINAAN TEKNIS"