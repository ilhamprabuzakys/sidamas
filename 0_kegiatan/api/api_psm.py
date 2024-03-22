from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from sidamas import pagination

from kegiatan import models
from kegiatan.api import serializers

# class PSM_RAKERNIS_ViewSet(viewsets.ModelViewSet):
#     queryset = models.PSM_RAKERNIS.objects.all()
#     serializer_class = serializers.PSM_RAKERNIS_Serializer
#     permission_classes = [permissions.IsAuthenticated]
#     pagination_class = pagination.Page10NumberPagination
#     filter_backends = [DjangoFilterBackend, ]
    
#     def get_view_name(self):
#         return "PSM RAKERNIS"

