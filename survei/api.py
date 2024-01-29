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
    
class tbl_responden_surveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_responden_survei class"""

    queryset = models.tbl_responden_survei.objects.all()
    serializer_class = serializers.tbl_responden_surveiSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_surveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_survei class"""

    queryset = models.tbl_survei.objects.all()
    serializer_class = serializers.tbl_surveiSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_data_respondenViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_data_responden class"""

    queryset = models.tbl_data_responden.objects.all()
    serializer_class = serializers.tbl_data_respondenSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Mengembalikan ID responden sebagai bagian dari respons
        response_data = serializer.data
        response_data['id_responden'] = serializer.instance.id

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class tbl_isi_surveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_isi_survei class"""

    queryset = models.tbl_isi_survei.objects.all()
    serializer_class = serializers.tbl_isi_surveiSerializer
    permission_classes = [permissions.IsAuthenticated]


class tbl_data_surveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the tbl_isi_survei class"""

    queryset = models.tbl_data_survei.objects.all()
    serializer_class = serializers.tbl_data_surveiSerializer
    permission_classes = [permissions.IsAuthenticated]