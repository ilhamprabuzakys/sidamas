from rest_framework import serializers

from . import models

# Percobaan
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

class DataSurveiSerializer(serializers.ModelSerializer):
    get_jumlah_responden = serializers.SerializerMethodField()
    get_status_keberlangsungan = serializers.SerializerMethodField()
    get_status_responden = serializers.SerializerMethodField()
    
    class Meta:
        model = models.DataSurvei
        fields = [
            "created_at",
            "updated_at",
            "id",
            "judul",
            "tanggal",
            "jam_awal",
            "jam_akhir",
            "batas_responden",
            "status_pengiriman",
            "kode",
            "get_jumlah_responden",
            "get_status_keberlangsungan",
            "get_status_responden",
            "tipe",
        ]
    
    def get_jumlah_responden(self, obj):
        return obj.get_jumlah_responden()
    
    def get_status_keberlangsungan(self, obj):
        return obj.get_status_keberlangsungan()
    
    def get_status_responden(self, obj):
        return obj.get_status_responden()
        
class DataSurveiDetailSerializer(serializers.ModelSerializer):
    jumlah_responden = serializers.SerializerMethodField()

    class Meta:
        model = models.DataSurvei
        fields = [
            "created_at",
            "updated_at",
            "id",
            "judul",
            "tanggal",
            "jam_awal",
            "jam_akhir",
            "batas_responden",
            "status_pengiriman",
            "jumlah_responden",
            "kode",
            "tipe",
        ]

    def jumlah_responden(self, obj):
        return obj.get_jumlah_responden()

class DataRespondenSurveiSerializer(serializers.ModelSerializer):
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
            
            "survei",
        ]

class DataPengisianSurveiSerializer(serializers.ModelSerializer):
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
        ]