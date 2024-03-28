from django.contrib.auth.models import User
import django_filters as filters
from django_filters.filters import Q

from . import models

class UsersFilter(filters.FilterSet):
    s = filters.CharFilter(method='filter_global_search', label='Global search')
    profile = filters.NumberFilter(field_name='profile__id', label='ID Profile')
    satker = filters.NumberFilter(field_name='profile__satker_id', label='ID Satuan Kerja')
    
    direktorat = filters.ChoiceFilter(field_name='profile__role', label='Direktorat', choices=models.Profile.DIREKTORAT_CHOICES)
    
    LEVEL_CHOICES = (
        (0, 'Provinsi'),
        (1, 'Kabupaten'),
        (2, 'Pusat')
    )
    
    satker_level = filters.ChoiceFilter(field_name='profile__satker__level', label='Level Satuan Kerja', choices=LEVEL_CHOICES)
    satker_parent = filters.NumberFilter(field_name='profile__satker__parent', label='Parent Satuan Kerja')
    
    class Meta:
        model = User
        fields = ['s', 'profile', 'satker', 'satker_level', 'satker_parent']
        
    def filter_global_search(self, queryset, name, value):
        return queryset.filter(
            Q(username__icontains=value) |
            Q(first_name__icontains=value) |
            Q(last_name__icontains=value)
        )
    