from rest_framework import serializers

from . import models

# Serializers using Model Serializer
class TipeSurveiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipeSurvei
        fields = [
            "created_at",
            "updated_at",
            "id",
            "nama",
            "daftar_pertanyaan",
        ]
       
# class DataSurveiDetailSerializer(serializers.ModelSerializer):
#     jumlah_responden = serializers.SerializerMethodField()

#     class Meta:
#         model = models.DataSurvei
#         fields = [
#             "created_at",
#             "updated_at",
#             "id",
#             "judul",
#             "tanggal",
#             "jam_awal",
#             "jam_akhir",
#             "batas_responden",
#             "status_pengiriman",
#             "jumlah_responden",
#             "kode",
#             "tipe",
#         ]

#     def jumlah_responden(self, obj):
#         return obj.get_jumlah_responden()

class DataRespondenSurveiSerializer(serializers.ModelSerializer):
    jenis_kelamin = serializers.ChoiceField(choices=models.DataRespondenSurvei.JENIS_KELAMIN_CHOICES, required=False)
    rentang_usia = serializers.ChoiceField(choices=models.DataRespondenSurvei.RENTANG_USIA_CHOICES, required=False)
    pendidikan = serializers.ChoiceField(choices=models.DataRespondenSurvei.PENDIDIKAN_CHOICES, required=False)

    class Meta:
        model = models.DataRespondenSurvei
        fields = [
            "created_at",
            "updated_at",
            "id",
            "jenis_kelamin",
            "rentang_usia",
            "pendidikan",
            "nama",
            "pekerjaan",
            "alamat",
            "handphone",
            "email",
            "survei",
        ]

class DataSurveiSerializer(serializers.ModelSerializer):
    
    get_jumlah_responden = serializers.SerializerMethodField()
    get_status_keberlangsungan = serializers.SerializerMethodField()
    get_status_responden = serializers.SerializerMethodField()
    get_data_isian = serializers.SerializerMethodField()
    get_data_tipe = serializers.SerializerMethodField()
    get_satker_name = serializers.SerializerMethodField()

    class Meta:
        model = models.DataSurvei
        # fields = '__all__'
        fields = [
            "created_at",
            "updated_at",
            "id",
            "judul",
            "tanggal_awal",
            "tanggal_akhir",
            "jam_awal",
            "jam_akhir",
            "batas_responden",
            "status_pengiriman",
            "kode",
            "get_jumlah_responden",
            "get_status_keberlangsungan",
            "get_status_responden",
            "get_data_isian",
            "get_data_tipe",
            "tipe",
            "satker",
            "get_satker_name",
            "keterangan",
            # "responden",
        ]
    
    def get_jumlah_responden(self, obj):
        return obj.get_jumlah_responden()
    
    def get_status_keberlangsungan(self, obj):
        return obj.get_status_keberlangsungan()
    
    def get_status_responden(self, obj):
        return obj.get_status_responden()
    
    def get_data_isian(self, obj):
        return obj.get_data_isian()
    
    def get_data_responden(self, obj):
        return obj.get_data_responden()
    
    def get_data_tipe(self, obj):
        return obj.get_data_tipe()
    
    def get_satker_name(self, obj):
        return obj.get_satker_name()
    
class DataPengisianSurveiSerializer(serializers.ModelSerializer):

    get_data_responden = serializers.SerializerMethodField()

    class Meta:
        model = models.DataPengisianSurvei
        fields = [
            "created_at",
            "updated_at",
            "id",
            "array_nilai_jawaban",
            "data_mentahan",
            "sigma_nilai",
            
            "survei",
            "responden",
            "get_data_responden",
        ]

    def get_data_responden(self, obj):
        return obj.get_data_responden()