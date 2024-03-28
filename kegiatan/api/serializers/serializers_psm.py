from rest_framework import serializers

from kegiatan import models
from users.models import Profile, Satker
from kegiatan.serializers import SatkerSerializer, UserSerializer


# ======= PSM RAKERNIS SERIALIZER =======    
class PSM_RAKERNIS_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_RAKERNIS
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'satker_target',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'dokumentasi', 'status'
        ]

class PSM_RAKERNIS_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_RAKERNIS
        exclude = []
        fields = [
            'id','satker', 'satker_target', 'data'
        ]
    
    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_RAKERNIS_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret
    
class PSM_RAKERNIS_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    #satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_RAKERNIS
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]
    
    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_RAKERNIS.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_RAKERNIS.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_RAKERNIS.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_RAKERNIS_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_RAKERNIS.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_RAKERNIS_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_RAKERNIS_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    satker_target = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())

    class Meta:
        model = models.PSM_RAKERNIS
        fields = '__all__'

# ======= PSM BINAAN TEKNIS SERIALIZER =======

class PSM_BINAAN_TEKNIS_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'satker_target',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'dokumentasi', 'status'
        ]

class PSM_BINAAN_TEKNIS_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        exclude = []
        fields = [
            'id','satker', 'satker_target', 'data'
        ]
    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_BINAAN_TEKNIS_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret
    
class PSM_BINAAN_TEKNIS_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    # satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]
    
    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')

        ret = PSM_BINAAN_TEKNIS_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_BINAAN_TEKNIS.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_BINAAN_TEKNIS_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_BINAAN_TEKNIS_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    satker_target = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())

    class Meta:
        model = models.PSM_BINAAN_TEKNIS
        fields = '__all__'

# ======= PSM ASISTENSI SERIALIZER =======
class PSM_ASISTENSI_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.PSM_ASISTENSI
        exclude = []
        fields = [
            'id','tanggal_awal', 'tanggal_akhir', 'satker', 'jumlah_kegiatan', 'jumlah_peserta', 'stakeholder',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'dokumentasi', 'status'
        ]

class PSM_ASISTENSI_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_ASISTENSI
        exclude = []
        fields = [
            'id','satker','data'
        ]
    
    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_ASISTENSI_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret
    
class PSM_ASISTENSI_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    #satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_ASISTENSI
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]
    
    def get_detail(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_ASISTENSI.objects.filter(satker__parent = obj.satker).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 0:
            # bnnp
            res = models.PSM_ASISTENSI.objects.filter(satker__parent = obj.satker, status__gt = 0).order_by('satker__id', 'satker__order').distinct('satker__id')
        elif satker_level == 2:
            # pusat
            res = models.PSM_ASISTENSI.objects.filter(satker__parent = obj.satker, status= 2).order_by('satker__id', 'satker__order').distinct('satker__id')
            
        ret = PSM_ASISTENSI_CHILD_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

    def get_data(self, obj):
        user_id = self.context['request'].user.id
        satker = Profile.objects.values_list('satker', flat=True).get(user_id=user_id)
        satker_level = Satker.objects.values_list('level', flat=True).get(id=satker)

        status = None
        if satker_level == 1:
            # bnnk
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker)
        elif satker_level == 0:
            # bnnp
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker, status__gt = 0)
        elif satker_level == 2:
            # pusat
            res = models.PSM_ASISTENSI.objects.filter(satker = obj.satker, status = 2)

        ret = PSM_ASISTENSI_DATA_Serializer(res, many=True, context={'request': self.context['request']}).data
        #print(ret)
        return ret

class PSM_ASISTENSI_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())

    class Meta:
        model = models.PSM_ASISTENSI
        fields = '__all__'
        
# ======= PSM TES URINE DETEKSI DINI SERIALIZER =======
class PSM_TES_URINE_DETEKSI_DINI_PESERTA_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI_PESERTA
        fields = ['id', 'parent', 'nama_peserta', 'jenis_kelamin', 'hasil_test', 'alamat']

    def __init__(self, *args, parent_id=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent_id = parent_id

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data

    def to_internal_value(self, data):
        data['parent'] = self.parent_id
        return super().to_internal_value(data)
    
class PSM_TES_URINE_DETEKSI_DINI_PESERTA_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI_PESERTA
        fields = ['id', 'parent', 'nama_peserta', 'jenis_kelamin', 'hasil_test', 'alamat']

class PSM_TES_URINE_DETEKSI_DINI_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    pegawai = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        exclude = []
        datatables_always_serialize = ['id', 'satker', 'nama_satker', 'jumlah_kegiatan', 'tanggal', 'nama_lingkungan', 'hasil_tes_urine', 'tindak_lanjut', 'dokumentasi', 'pegawai']

    def get_pegawai(self, obj):
        parent_id = obj.id
        pegawai_objects = models.PSM_TES_URINE_DETEKSI_DINI_PESERTA.objects.filter(parent=parent_id)
        ret = PSM_TES_URINE_DETEKSI_DINI_PESERTA_Serializer(pegawai_objects, many=True).data
        return ret

class PSM_TES_URINE_DETEKSI_DINI_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        exclude = []
        fields = [
            'id','satker', 'satker_target', 'data'
        ]
    def get_data(self, obj):
        res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker = obj.satker)
        ret = PSM_TES_URINE_DETEKSI_DINI_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret

class PSM_TES_URINE_DETEKSI_DINI_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    # satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        exclude = []
        fields = [
            'id','satker','data','detail'
        ]

    def get_data(self, obj):
        res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker = obj.satker)
        ret = PSM_TES_URINE_DETEKSI_DINI_DATA_Serializer(res, many=True).data
        #print(ret)
        return ret
    
    def get_detail(self, obj):
        res = models.PSM_TES_URINE_DETEKSI_DINI.objects.filter(satker__parent = obj.satker).order_by('satker__id').distinct('satker__id')
        ret = PSM_TES_URINE_DETEKSI_DINI_CHILD_Serializer(res, many=True).data
        #print(ret)
        return ret
    
class PSM_TES_URINE_DETEKSI_DINI_CREATE_UPDATE_Serializer(serializers.ModelSerializer):
    dokumentasi = serializers.FileField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    class Meta:
        model = models.PSM_TES_URINE_DETEKSI_DINI
        fields = ['id', 'satker', 'satker_target', 'tanggal_awal', 'tanggal_akhir', 'nama_lingkungan', 'tindak_lanjut', 'dokumentasi']


# ======= PSM RAKOR PEMETAAN SERIALIZER =======
class PSM_BINAAN_TEKNIS_CRUD_Serializer(serializers.ModelSerializer):
    satker = serializers.PrimaryKeyRelatedField(queryset=Satker.objects.all())
    class Meta:
        model = models.PSM_RAKOR_PEMETAAN
        fields = '__all__'