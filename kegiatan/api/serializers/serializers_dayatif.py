from rest_framework import serializers

from kegiatan import models
from kegiatan.serializers import SatkerSerializer, UserSerializer

# BINAAN TEKNIS OLD
class DAYATIF_BINAAN_TEKNIS_DETAIL_Serializer(serializers.Serializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)
    updated_by = UserSerializer(many=False, read_only=True)

class DAYATIF_BINAAN_TEKNIS_Serializer(serializers.ModelSerializer):
    
    detail = DAYATIF_BINAAN_TEKNIS_DETAIL_Serializer(many=False, read_only=True, source='*')

    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        exclude = []
        datatables_always_serialize = ['tanggal_awal', 'tanggal_akhir', 'status']
        
# PEMETAAN POTENSI
class DAYATIF_PEMETAAN_POTENSI_DETAIL_Serializer(serializers.Serializer):
    satker = SatkerSerializer(many=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)
    updated_by = UserSerializer(many=False, read_only=True)

class DAYATIF_PEMETAAN_POTENSI_Serializer(serializers.ModelSerializer):
    
    detail = DAYATIF_PEMETAAN_POTENSI_DETAIL_Serializer(many=False, read_only=True, source='*')

    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        exclude = []
        datatables_always_serialize = ['tanggal_awal', 'tanggal_akhir', 'nama_desa', 'nama_kecamatan', 'nama_kabupaten', 'nama_provinsi']
        

