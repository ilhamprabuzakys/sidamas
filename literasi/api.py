from rest_framework import viewsets, permissions

from . import serializers
from . import models


class LiterasiViewSet(viewsets.ModelViewSet):
    """ViewSet for the literasi class"""

    queryset = models.Literasi.objects.all()
    serializer_class = serializers.LiterasiSerializer
    permission_classes = [permissions.IsAuthenticated]
