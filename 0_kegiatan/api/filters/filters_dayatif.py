import django_filters as filters
from django_filters.filters import Q

from kegiatan import models

# class DAYATIF_BINAAN_TEKNIS_Filters(filters.FilterSet):
#     satker = filters.NumberFilter(field_name='satker', label='Satker Pelaksana ID')
#     satker_target = filters.NumberFilter(field_name='satker_target', label='Satker Target ID')
#     s = filters.CharFilter(method='filter_global_search', label='Global search')

#     class Meta:
#         model = models.DAYATIF_BINAAN_TEKNIS
#         fields = ['satker', 's']
#         order_by = ['-satker__nama_satker']

#     def filter_global_search(self, queryset, name, value):
#         return queryset.filter(
#             Q(satker__nama_satker__icontains=value) |
#             Q(satker_target__nama_satker__icontains=value)
#         )