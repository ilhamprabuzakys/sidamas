import django_filters as filters
from django_filters.filters import Q

from kegiatan import models

class PSM_RAKERNIS_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')
    satker_target = filters.NumberFilter(field_name='satker_target', label='Satker Target ID')

    class Meta:
        model = models.PSM_RAKERNIS
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value) |
            Q(satker_target__nama_satker__icontains=value)
        )
    
class PSM_BINAAN_TEKNIS_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')
    satker_target = filters.NumberFilter(field_name='satker_target', label='Satker Target ID')

    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value) |
            Q(satker_target__nama_satker__icontains=value)
        )

class PSM_ASISTENSI_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_ASISTENSI
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value) 
        )
    
class PSM_TES_URINE_DETEKSI_DINI_Filters(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')

    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        fields = ['s', 'satker']
        order_by = ['-satker__nama_satker']

    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(s__deskripsi__icontains=value) |
            Q(satker__nama_satker__icontains=value) 
        )