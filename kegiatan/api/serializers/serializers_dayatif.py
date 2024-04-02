from rest_framework import serializers

from kegiatan import models
from kegiatan.serializers import SatkerSerializer, UserSerializer
from users.models import Profile, Satker

# ======= BINAAN TEKNIS =======
class DAYATIF_BINAAN_TEKNIS_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        depth = 1
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super(DAYATIF_BINAAN_TEKNIS_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

# =======  BINAAN TEKNIS LIST =======
class DAYATIF_BINAAN_TEKNIS_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    
    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        exclude = []

class DAYATIF_BINAAN_TEKNIS_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    satker_target = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        fields = ['id','satker', 'satker_target', 'data']
    
    def get_data(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level

        if satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_BINAAN_TEKNIS.objects.filter(satker=obj.satker, status__gt=0).order_by('-tanggal_awal')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_BINAAN_TEKNIS.objects.filter(satker=obj.satker, status=2).order_by('-tanggal_awal')

        serialized_data = DAYATIF_BINAAN_TEKNIS_LIST_DATA_Serializer(queryset, many=True).data
        print('[LIST_CHILD] [DATA] Serialized data:', len(serialized_data))
        return serialized_data
    
class DAYATIF_BINAAN_TEKNIS_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_BINAAN_TEKNIS
        fields = ['id','satker','data','detail']
    
    
    def get_data(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level
        
        if satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_BINAAN_TEKNIS.objects.filter(satker=obj.satker, status__gt=0).order_by('-tanggal_awal')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_BINAAN_TEKNIS.objects.filter(satker=obj.satker, status=2).order_by('-tanggal_awal')

        serialized_data = DAYATIF_BINAAN_TEKNIS_LIST_DATA_Serializer(queryset, many=True, context=self.context).data
        print('[LIST] [DATA] Serialized data:', len(serialized_data))
        return serialized_data
    
    def get_detail(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level

        if satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_BINAAN_TEKNIS.objects.filter(satker__parent=obj.satker, status__gt=0).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_BINAAN_TEKNIS.objects.filter(satker__parent=obj.satker, status=2).order_by('satker__order', '-tanggal_awal').distinct('satker__order')

        serialized_data = DAYATIF_BINAAN_TEKNIS_LIST_CHILD_Serializer(queryset, many=True, context=self.context).data
        print('[LIST] [DETAIL] Serialized data:', len(serialized_data))
        return serialized_data
        
# ======= PEMETAAN POTENSI =======
class DAYATIF_PEMETAAN_POTENSI_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        depth = 1
        exclude = []
        
    def __init__(self, *args, **kwargs):
        super(DAYATIF_PEMETAAN_POTENSI_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
    
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
        fields = ['id', 'satker', 'data']
        
    
    def get_data(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level

        if satker_level == 1:
            # BNNK
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker=obj.satker).order_by('-tanggal_awal')
        elif satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker=obj.satker, status__gt=0).order_by('-tanggal_awal')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker=obj.satker, status=2).order_by('-tanggal_awal')

        serialized_data = DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer(queryset, many=True).data
        print('[LIST_CHILD] [DATA] Serialized data:', len(serialized_data))
        return serialized_data

class DAYATIF_PEMETAAN_POTENSI_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_PEMETAAN_POTENSI
        fields = ['id', 'satker', 'data', 'detail']
        
    def get_data(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level

        if satker_level == 1:
            # BNNK
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker=obj.satker).order_by('-tanggal_awal')
        elif satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker=obj.satker, status__gt=0).order_by('-tanggal_awal')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker=obj.satker, status=2).order_by('-tanggal_awal')

        serialized_data = DAYATIF_PEMETAAN_POTENSI_LIST_DATA_Serializer(queryset, many=True).data
        print('[LIST_CHILD] [DATA] Serialized data:', len(serialized_data))
        return serialized_data
        
    def get_detail(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level
        
        if satker_level == 1:
            # BNNK
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent=obj.satker).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
        elif satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent=obj.satker, status__gt = 0).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker__parent=obj.satker, status= 2).order_by('satker__order', '-tanggal_awal').distinct('satker__order')

        serialized_data = DAYATIF_PEMETAAN_POTENSI_LIST_CHILD_Serializer(queryset, many=True, context=self.context).data
        print('[LIST] [DETAIL] Serialized data:', len(serialized_data))
        return serialized_data
    
# ======= PEMETAAN STAKEHOLDER =======
class DAYATIF_PEMETAAN_STAKEHOLDER_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.DAYATIF_PEMETAAN_STAKEHOLDER
        depth = 1
        exclude = []
        
    def __init__(self, *args, **kwargs):
        super(DAYATIF_PEMETAAN_STAKEHOLDER_Serializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method=='POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1
    
# ======= PEMETAAN STAKEHOLDER LIST =======
class DAYATIF_PEMETAAN_STAKEHOLDER_LIST_DATA_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    class Meta:
        model = models.DAYATIF_PEMETAAN_STAKEHOLDER
        exclude = []

class DAYATIF_PEMETAAN_STAKEHOLDER_LIST_CHILD_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_PEMETAAN_STAKEHOLDER
        fields = ['id', 'satker', 'data']
        
    
    def get_data(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level

        if satker_level == 1:
            # BNNK
            queryset = models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.filter(satker=obj.satker).order_by('-tanggal_awal')
        elif satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.filter(satker=obj.satker, status__gt=0).order_by('-tanggal_awal')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.filter(satker=obj.satker, status=2).order_by('-tanggal_awal')

        serialized_data = DAYATIF_PEMETAAN_STAKEHOLDER_LIST_DATA_Serializer(queryset, many=True).data
        print('[LIST_CHILD] [DATA] Serialized data:', len(serialized_data))
        return serialized_data

class DAYATIF_PEMETAAN_STAKEHOLDER_LIST_Serializer(serializers.ModelSerializer):
    satker = SatkerSerializer(many=False, read_only=True)
    data = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()

    class Meta:
        model = models.DAYATIF_PEMETAAN_STAKEHOLDER
        fields = ['id', 'satker', 'data', 'detail']
        
    def get_data(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level

        if satker_level == 1:
            # BNNK
            queryset = models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.filter(satker=obj.satker).order_by('-tanggal_awal')
        elif satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.filter(satker=obj.satker, status__gt=0).order_by('-tanggal_awal')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.filter(satker=obj.satker, status=2).order_by('-tanggal_awal')

        serialized_data = DAYATIF_PEMETAAN_STAKEHOLDER_LIST_DATA_Serializer(queryset, many=True).data
        print('[LIST_CHILD] [DATA] Serialized data:', len(serialized_data))
        return serialized_data
        
    def get_detail(self, obj):
        request = self.context.get('request')
        satker_level = request.user.profile.satker.level
        
        if satker_level == 1:
            # BNNK
            queryset = models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.filter(satker__parent=obj.satker).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
        elif satker_level == 0:
            # BNNP
            queryset = models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.filter(satker__parent=obj.satker, status__gt = 0).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
        elif satker_level == 2:
            # PUSAT
            queryset = models.DAYATIF_PEMETAAN_STAKEHOLDER.objects.filter(satker__parent=obj.satker, status= 2).order_by('satker__order', '-tanggal_awal').distinct('satker__order')

        serialized_data = DAYATIF_PEMETAAN_STAKEHOLDER_LIST_CHILD_Serializer(queryset, many=True, context=self.context).data
        print('[LIST] [DETAIL] Serialized data:', len(serialized_data))
        return serialized_data