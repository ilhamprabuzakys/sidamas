from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from . import serializers
from . import models

# Percobaan
class TipeSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the TipeSurvei class"""

    queryset = models.TipeSurvei.objects.all()
    serializer_class = serializers.TipeSurveiSerializer
    permission_classes = [permissions.IsAuthenticated]

class DataSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataSurvei class"""

    queryset = models.DataSurvei.objects.all()
    serializer_class = serializers.DataSurveiSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        kode_value = self.request.query_params.get('kode')
        if kode_value:
            return models.DataSurvei.objects.filter(kode=kode_value)
        
        return models.DataSurvei.objects.all()
    
    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return serializers.DataSurveiDetailSerializer
    #     return serializers.DataSurveiSerializer

class DataRespondenSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataRespondenSurvei class"""

    queryset = models.DataRespondenSurvei.objects.all()
    serializer_class = serializers.DataRespondenSurveiSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        survei_id = self.request.query_params.get('survei')
        if survei_id:
            return models.DataRespondenSurvei.objects.filter(survei=survei_id)
        return models.DataRespondenSurvei.objects.all()

class DataPengisianSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataPengisianSurvei class"""

    queryset = models.DataPengisianSurvei.objects.all()
    serializer_class = serializers.DataPengisianSurveiSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        responden_id = self.request.query_params.get('responden')
        if responden_id:
            return models.DataPengisianSurvei.objects.filter(responden=responden_id)
            return models.DataPengisianSurvei.objects.get(responden=responden_id)
            
        
        return models.DataPengisianSurvei.objects.all()