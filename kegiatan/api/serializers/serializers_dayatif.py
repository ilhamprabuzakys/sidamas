from rest_framework import serializers

from kegiatan import models
from kegiatan.serializers import SatkerSerializer, UserSerializer
from users.models import Profile, Satker

# ======= BINAAN TEKNIS =======
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
        
# ======= PEMETAAN POTENSI =======
class DAYATIF_PEMETAAN_POTENSI_Serializer(serializers.ModelSerializer):
    # satker = serializers.PrimaryKeyRelatedField(queryset=models.Satker.objects.all())
    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        depth = 1
        exclude = []
    
# ======= PEMETAAN POTENSI LIST =======
class DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        exclude = []

class DAYATIF_PEMETAAN_POTENSI_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        fields = [ 'id','satker', 'data' ]
        
    
    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker = obj.satker, status = 2)

        ret = DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret
    
    def get_data(self, obj):
        res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker = obj.satker, status__gt=0)
        ret = DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer(res, many=True).data
        return ret

class DAYATIF_PEMETAAN_POTENSI_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        exclude = []
        fields = [ 'id','satker','data','detail' ]
        
    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = DAYATIF_PEMETAAN_POTENSI_LIST_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker = obj.satker, status = 2)

        ret = DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret
    
    # def get_detail(self, obj):
    #     res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent = obj.satker).order_by('satker__id').distinct('satker__id')
    #     ret = DAYATIF_PEMETAAN_POTENSI_LIST_CHILD_Serializer(res, many=True).data
    #     return ret

    # def get_data(self, obj):
    #     res = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker = obj.satker)
    #     ret = DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer(res, many=True).data
    #     #print(ret)
    #     return ret