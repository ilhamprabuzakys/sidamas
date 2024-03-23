from rest_framework import serializers

from kegiatan import models
from kegiatan.serializers import SatkerSerializer, UserSerializer

class PSM_RAKERNIS_DETAIL_Serializer(serializers.Serializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)
    updated_by = UserSerializer(many=False, read_only=True)
    
class PSM_RAKERNIS_Serializer(serializers.ModelSerializer):
    detail = PSM_RAKERNIS_DETAIL_Serializer(many=False, read_only=True, source='*')
    
    class Meta:
        model = models.PSM_RAKERNIS
        exclude = []
        datatables_always_serialize = ['id', 'satker_id', 'satker_target', 'nama_satker_target', 'nama_satker', 'tanggal_awal', 'tanggal_akhir',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'dokumentasi', 'status', 'satker_level']
        

class PSM_BINAAN_TEKNIS_DETAIL_Serializer(serializers.Serializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)
    updated_by = UserSerializer(many=False, read_only=True)
    
class PSM_BINAAN_TEKNIS_Serializer(serializers.ModelSerializer):
    detail = PSM_BINAAN_TEKNIS_DETAIL_Serializer(many=False, read_only=True, source='*')
    
    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        exclude = []
        datatables_always_serialize = ['id', 'satker_id', 'satker_target', 'nama_satker_target', 'nama_satker', 'tanggal_awal', 'tanggal_akhir',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'dokumentasi', 'status', 'satker_level']

class PSM_ASISTENSI_DETAIL_Serializer(serializers.Serializer):
    satker = SatkerSerializer(many=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)
    updated_by = UserSerializer(many=False, read_only=True)

class PSM_ASISTENSI_Serializer(serializers.ModelSerializer):
    detail = PSM_ASISTENSI_DETAIL_Serializer(many=False, read_only=True, source='*')
    
    class Meta:
        model = models.PSM_ASISTENSI
        exclude = []
        datatables_always_serialize = ['id', 'satker_id', 'nama_satker', 'jumlah_kegiatan', 'tanggal', 'jumlah_peserta', 'stakeholder',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'dokumentasi']
        
class PSM_TES_URINE_DETEKSI_DINI_DETAIL_Serializer(serializers.Serializer):
    satker = SatkerSerializer(many=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)
    updated_by = UserSerializer(many=False, read_only=True)

class PSM_TES_URINE_DETEKSI_DINI_Serializer(serializers.ModelSerializer):
    detail = PSM_TES_URINE_DETEKSI_DINI_DETAIL_Serializer(many=False, read_only=True, source='*')
    
    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        exclude = []
        datatables_always_serialize = ['id', 'satker_id', 'nama_satker', 'jumlah_kegiatan', 'tanggal', 'nama_lingkungan', 'hasil_tes_urine', 'tindak_lanjut', 'dokumentasi']