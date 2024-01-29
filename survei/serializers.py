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
            "jumlah_responden",
            "status",
            "kode",
            
            "tipe",
        ]

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
        
class tbl_responden_surveiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tbl_responden_survei
        fields = [
            "last_updated",
            "pendidikan",
            "jawaban",
            "id_survei",
            "nama",
            "jenis_kelamin",
            "perusahaan",
            "created",
            "pekerjaan",
        ]


class tbl_surveiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tbl_survei
        fields = [
            "tanggal",
            "url",
            "created",
            "jam_awal",
            "last_updated",
            "role",
            "tipe",
            "judul",
            "status",
            "jam_akhir",
        ]


class tbl_data_respondenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tbl_data_responden
        fields = [
            "id",  # Menambahkan ID
            "created",
            "rentang_usia",
            "pendidikan_terkahir",
            "last_updated",
            "jenis_kelamin",
        ]


class tbl_isi_surveiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tbl_isi_survei
        fields = [
            "id",
            "id_data_survei",
            "id_data_responden",
            "last_updated",
            "array_nilai_jawaban",
            "created",
            "data_mentahan",
            "sigma_nilai",
        ]

class tbl_data_surveiSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.tbl_data_survei
        fields = [
            "id",
            "nama",
            "tipe",
            "tanggal",
            "daftar_pertanyaan",
            "jam_awal",
            "jam_akhir",
            "jumlah_responden",
            "status",
            "kode",
            "created",
            "updated",
        ]
        