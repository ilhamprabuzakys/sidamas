from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.core import exceptions as django_exceptions
from rest_framework.decorators import action
from rest_framework_datatables.pagination import DatatablesPageNumberPagination
from rest_framework_datatables.django_filters.backends import DatatablesFilterBackend
from rest_framework_datatables.django_filters.filterset import DatatablesFilterSet
from rest_framework_datatables.django_filters.filters import GlobalFilter
from django.core import serializers
from django.db.models import Q
import json
import ast

from . import serializers
from . import models

class CustomDatatablePagination(DatatablesPageNumberPagination):
    page_size = 100
    
class TipeSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the TipeSurvei class"""

    queryset = models.TipeSurvei.objects.all()
    serializer_class = serializers.TipeSurveiSerializer

class DataSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataSurvei class"""

    queryset = models.DataSurvei.objects.all()
    serializer_class = serializers.DataSurveiSerializer
    filter_backends = [filters.DjangoFilterBackend,]
    # filterset_fields = ('id',)
    pagination_class = CustomDatatablePagination
    
    # permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        kode_value = self.request.query_params.get('kode')
        if kode_value:
            return models.DataSurvei.objects.filter(kode=kode_value)
        
        return models.DataSurvei.objects.all()
    
    # def get_serializer_class(self):
    #     if self.action == 'retrieve':
    #         return serializers.DataSurveiDetailSerializer
    #     return serializers.DataSurveiSerializer

    @action(detail=False, methods=['post'])  # Change detail to False for actions not related to a single instance
    def triwulan(self, request):
        try:
            triwulan = request.data.get('triwulan')
            tipe = request.data.get('tipe')
            tipe_survei = models.TipeSurvei.objects.get(nama=tipe)

            triwulan_json = json.dumps(triwulan)
            
            triwulan_lista = json.loads(triwulan_json)

            months = triwulan_lista[0]
            year = triwulan_lista[1]
            satker = triwulan_lista[2]
            
            month_filters = Q()
            for month in months:
                month_filters |= Q(created_at__month=month, created_at__year=year)

            if satker == 0:
                data_survei_queryset = models.DataSurvei.objects.filter(month_filters, tipe = tipe_survei.id)
            else:
                data_survei_queryset = models.DataSurvei.objects.filter(month_filters, tipe = tipe_survei.id, satker=satker)

            serialized_data = self.serializer_class(data_survei_queryset, many=True).data
            
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Survei not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['get'])  # Change detail to False for actions not related to a single instance
    def life_skill(self, request):
        try:
            tipe_survei = models.TipeSurvei.objects.get(nama="SKM Life Skill")

            data_survei_queryset = models.DataSurvei.objects.filter(tipe=tipe_survei.id)
            serialized_data = self.serializer_class(data_survei_queryset, many=True).data
            
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Survei not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['get'])  # Change detail to False for actions not related to a single instance
    def test_urine(self, request):
        try:
            tipe_survei = models.TipeSurvei.objects.get(nama="SKM Tes Urine")

            data_survei_queryset = models.DataSurvei.objects.filter(tipe=tipe_survei.id)
            serialized_data = self.serializer_class(data_survei_queryset, many=True).data
            
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Survei not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=False, methods=['get'])  # Change detail to False for actions not related to a single instance
    def keberhasilan_kewirausahaan(self, request):
        try:
            tipe_survei = models.TipeSurvei.objects.get(nama="Keberhasilan dan Kewirausahaan")

            data_survei_queryset = models.DataSurvei.objects.filter(tipe=tipe_survei.id)
            serialized_data = self.serializer_class(data_survei_queryset, many=True).data
            
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Survei not found.'}, status=status.HTTP_404_NOT_FOUND)
    

class DataRespondenSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataRespondenSurvei class"""

    queryset = models.DataRespondenSurvei.objects.all()
    serializer_class = serializers.DataRespondenSurveiSerializer
    filterset_fields = ('survei',)
    filter_backends = (filters.DjangoFilterBackend,)
    
    def get_queryset(self):
        survei_id = self.request.query_params.get('survei')
        if survei_id:
            return models.DataRespondenSurvei.objects.filter(survei=survei_id)
        return models.DataRespondenSurvei.objects.all()
    
    @action(detail=False, methods=['post'])  # Change detail to False for actions not related to a single instance
    def get_nama(self, request):
        try:
            nama = request.data.get('nama')

            responden = models.DataRespondenSurvei.objects.get(nama=nama)
            
            return Response({'data': True}, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'data': False}, status=status.HTTP_200_OK)

class DataPengisianSurveiViewSet(viewsets.ModelViewSet):
    """ViewSet for the DataPengisianSurvei class"""

    queryset = models.DataPengisianSurvei.objects.all()
    serializer_class = serializers.DataPengisianSurveiSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('responden', 'survei',)

    @action(detail=False, methods=['post'])  # Change detail to False for actions not related to a single instance
    def triwulan(self, request):
        try:
            triwulan = request.data.get('triwulan')
            
            triwulan_json = json.dumps(triwulan)
            
            triwulan_lista = json.loads(triwulan_json)

            months = triwulan_lista[0]
            year = triwulan_lista[1]
            
            month_filters = Q()
            for month in months:
                month_filters |= Q(created_at__month=month, created_at__year=year)

            data_survei_queryset = models.DataPengisianSurvei.objects.filter(month_filters)
            serialized_data = self.serializer_class(data_survei_queryset, many=True).data
            
            return Response(data=serialized_data, status=status.HTTP_200_OK)
        except django_exceptions.ObjectDoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)