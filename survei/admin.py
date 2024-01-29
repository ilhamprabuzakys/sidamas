from django.contrib import admin
from django import forms

from . import models
from . import forms as survei_forms

# Percobaan
class TipeSurveiAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'daftar_pertanyaan']
    readonly_fields = ['created_at', 'updated_at']
    
    form = survei_forms.TipeSurveiForm

class DataRespondenSurveiAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'jenis_kelamin', 'rentang_usia', 'pendidikan', 'pekerjaan']
    readonly_fields = ['created_at', 'updated_at']
    
    form = survei_forms.DataRespondenSurveiForm

class DataSurveiAdmin(admin.ModelAdmin):
    list_display = ['id', 'judul', 'tanggal', 'jam_awal', 'jam_akhir', 'jumlah_responden', 'kode']
    readonly_fields = ['created_at', 'updated_at']
    
    form = survei_forms.DataSurveiForm
    
class DataPengisianSurveiAdmin(admin.ModelAdmin):
    list_display = ['id', 'array_nilai_jawaban', 'data_mentahan', 'sigma_nilai']
    readonly_fields = ['created_at', 'updated_at']
    
    form = survei_forms.DataPengisianSurveiForm
    
admin.site.register(models.TipeSurvei, TipeSurveiAdmin)
admin.site.register(models.DataRespondenSurvei, DataRespondenSurveiAdmin)
admin.site.register(models.DataSurvei, DataSurveiAdmin)
admin.site.register(models.DataPengisianSurvei, DataPengisianSurveiAdmin)


class tbl_responden_surveiAdminForm(forms.ModelForm):

    class Meta:
        model = models.tbl_responden_survei
        fields = "__all__"


class tbl_responden_surveiAdmin(admin.ModelAdmin):
    form = tbl_responden_surveiAdminForm
    list_display = [
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
    readonly_fields = [
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


class tbl_surveiAdminForm(forms.ModelForm):

    class Meta:
        model = models.tbl_survei
        fields = "__all__"


class tbl_surveiAdmin(admin.ModelAdmin):
    form = tbl_surveiAdminForm
    list_display = [
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
    readonly_fields = [
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

class tbl_data_surveiAdmin(admin.ModelAdmin):
    list_display = ["nama", "tipe", "created", "updated"]
    readonly_fields = ["created", "updated"]
    
admin.site.register(models.tbl_responden_survei, tbl_responden_surveiAdmin)
admin.site.register(models.tbl_survei, tbl_surveiAdmin)
admin.site.register(models.tbl_data_survei, tbl_data_surveiAdmin)
