def get_list_data(self, obj, model_class, serializer_class):
    request = self.context.get('request')
    satker_level = request.user.profile.satker.level

    if satker_level == 1:
        # BNNK
        queryset = model_class.objects.filter(satker=obj.satker).order_by('-tanggal_awal')
    elif satker_level == 0:
        # BNNP
        queryset = model_class.objects.filter(satker=obj.satker, status__gt=0).order_by('-tanggal_awal')
    elif satker_level == 2:
        # PUSAT
        queryset = model_class.objects.filter(satker=obj.satker, status=2).order_by('-tanggal_awal')

    serialized_data = serializer_class(queryset, many=True).data
    print('[LIST_CHILD] [DATA] Serialized data:', len(serialized_data))
    return serialized_data

def get_list_detail(self, obj, model_class, serializer_class):
    request = self.context.get('request')
    satker_level = request.user.profile.satker.level
    
    if satker_level == 1:
        # BNNK
        queryset = model_class.objects.filter(satker__parent=obj.satker).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
    elif satker_level == 0:
        # BNNP
        queryset = model_class.objects.filter(satker__parent=obj.satker, status__gt=0).order_by('satker__order', '-tanggal_awal').distinct('satker__order')
    elif satker_level == 2:
        # PUSAT
        queryset = model_class.objects.filter(satker__parent=obj.satker, status=2).order_by('satker__order', '-tanggal_awal').distinct('satker__order')

    serialized_data = serializer_class(queryset, many=True, context=self.context).data
    print('[LIST] [DETAIL] Serialized data:', len(serialized_data))
    return serialized_data