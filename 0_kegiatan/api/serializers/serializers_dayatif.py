from rest_framework import serializers

from kegiatan import models
from kegiatan.serializers import SatkerSerializer, UserSerializer

class DAYATIF_BINAAN_TEKNIS_DETAIL_Serializer(serializers.Serializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    created_by = UserSerializer(many=False, read_only=True)
    updated_by = UserSerializer(many=False, read_only=True)

# class DAYATIF_BINAAN_TEKNIS_Serializer(serializers.ModelSerializer):
    
#     detail = DAYATIF_BINAAN_TEKNIS_DETAIL_Serializer(many=False, read_only=True, source='*')
#     # total_kegiatan = serializers.SerializerMethodField()

#     class Meta:
#         model = models.DAYATIF_BINAAN_TEKNIS
#         exclude = []
#         datatables_always_serialize = ['tanggal_awal', 'tanggal_akhir']
    
    # def get_total_kegiatan(self, obj):
    #     return obj.dayatif_kegiatan_binaan_teknis.count()

# class DAYATIF_KEGIATAN_BINAAN_TEKNIS_Serializer(serializers.ModelSerializer):
    
#     detail = DetailSerializer(many=False, read_only=True, source='*')

#     class Meta:
#         model = models.DAYATIF_KEGIATAN_BINAAN_TEKNIS
#         exclude = []
        #  datatables_always_serialize = ['tanggal_awal', 'tanggal_akhir']
