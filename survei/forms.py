from django import forms
from . import models


class tbl_responden_surveiForm(forms.ModelForm):
    class Meta:
        model = models.tbl_responden_survei
        fields = [
            "pendidikan",
            "jawaban",
            "id_survei",
            "nama",
            "jenis_kelamin",
            "perusahaan",
            "pekerjaan",
        ]


class tbl_surveiForm(forms.ModelForm):
    class Meta:
        model = models.tbl_survei
        fields = [
            "tanggal",
            "url",
            "jam_awal",
            "role",
            "tipe",
            "judul",
            "status",
            "jam_akhir",
        ]


class tbl_data_respondenForm(forms.ModelForm):
    class Meta:
        model = models.tbl_data_responden
        fields = [
            "rentang_usia",
            "pendidikan_terkahir",
            "jenis_kelamin",
        ]


class tbl_isi_surveiForm(forms.ModelForm):
    class Meta:
        model = models.tbl_isi_survei
        fields = [
            "array_nilai_jawaban",
            "data_mentahan",
            "sigma_nilai",
            "id_data_responden",
        ]

# Percobaan
class TipeSurveiForm(forms.ModelForm):
    class Meta:
        model = models.TipeSurvei
        fields = "__all__"
        # fields = [
        #     "nama",
        #     "daftar_pertanyaan",
        # ]
        
class DataRespondenSurveiForm(forms.ModelForm):
    class Meta:
        model = models.DataRespondenSurvei
        fields = "__all__"
        # fields = [
        #     "jenis_kelamin",
        #     "rentang_usia",
        #     "pendidikan",
        #     "nama",
        #     "pekerjaan",
        # ]
        
class DataSurveiForm(forms.ModelForm):
    class Meta:
        model = models.DataSurvei
        fields = "__all__"
        # fields = [
        #     "judul",
        #     "tanggal",
        #     "jam_awal",
        #     "jam_akhir",
        #     "jumlah_responden",
        #     "kode",
        # ]

class DataPengisianSurveiForm(forms.ModelForm):
    class Meta:
        model = models.DataSurvei
        fields = "__all__"
        # fields = [
        #     "array_nilai_jawaban",
        #     "data_mentahan",
        #     "sigma_nilai",
        # ]

