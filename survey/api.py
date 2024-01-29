from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from . import serializers
from . import models

class surveyViewSet(viewsets.ModelViewSet):
    """ViewSet for the kategori class"""

    queryset = models.survey.objects.all()
    serializer_class = serializers.survey
    #permission_classes = [permissions.IsAuthenticated]
class surveycreateViewSet(viewsets.ModelViewSet):
    """ViewSet for the kategori class"""

    queryset = models.survey.objects.all()
    serializer_class = serializers.survey_create
    #permission_classes = [permissions.IsAuthenticated]


class surveyshortViewSet(viewsets.ModelViewSet):
    """ViewSet for the berita class"""

    queryset = models.surveyshort.objects.all()
    serializer_class = serializers.surveyshort
    #permission_classes = [permissions.IsAuthenticated]


class survey_resultViewSet(viewsets.ModelViewSet):
    """ViewSet for the berita class"""

    queryset = models.survey_result.objects.all()
    serializer_class = serializers.survey_result
    #permission_classes = [permissions.IsAuthenticated]