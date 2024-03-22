from rest_framework import serializers
from django.contrib.auth.models import User
# from django_select2.forms import ModelSelect2Widget

from . import models

class ProfileSerializer(serializers.ModelSerializer):

    get_data_user_profil = serializers.SerializerMethodField()
    get_data_user_satker = serializers.SerializerMethodField()

    class Meta:
        model = models.Profile
        fields = [
            "id",
            "avatar",
            "user",
            "role",
            "satker",
            "is_verified",
            "get_data_user_profil",
            "get_data_user_satker",
        ]
        extra_kwargs = {'user': {'required': False}}

    def get_data_user_profil(self, obj):
        return obj.get_data_user_profil()
    
    def get_data_user_satker(self, obj):
        return obj.get_data_user_satker()

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_staff']

class SatkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Satker
        fields = [
            "id",
            "nama_satker",
            "parent",
            "level",
        ]

class reg_provincesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.reg_provinces
        fields = [
            "id",
            "kode_provinsi",
            "nama_provinsi",
        ]

class reg_regenciesSerializer(serializers.ModelSerializer):
    kode_provinsi = serializers.PrimaryKeyRelatedField(queryset=models.reg_provinces.objects.all())
    class Meta:
        model = models.reg_regencies
        fields = [
            "id",
            "kode_kabupaten",
            "kode_provinsi",
            "nama_kabupaten",
        ]

class reg_districtSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.reg_district
        fields = [
            "id",
            "kode_kecamatan",
            "kode_kabupaten",
            "nama_kecamatan",
        ]

class reg_villagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.reg_villages
        fields = [
            "id",
            "kode_desa",
            "kode_kecamatan",
            "nama_desa",
        ]