from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

from users.models import Satker

# class PSM_RAKERNIS(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(auto_now=True, editable=False)
    
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakernis_created_by")
#     updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakernis_updated_by")
    
#     satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_rakernis_satker", verbose_name="SATUAN KERJA PELAKSANA")
#     satker_target = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_rakernis_satker_target", verbose_name="SATUAN KERJA TARGET")
    
#     tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default='2024-03-18')
#     tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default='2024-03-18')
    
#     deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
#     kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
#     kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
#     tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
#     dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/rakernis/")
    
#     class Meta:
#         ordering = ['-updated_at']
#         verbose_name = 'PSM RAKERNIS'
#         verbose_name_plural = f'DAFTAR {verbose_name}'
#         db_table = 'kegiatan_psm_rakernis'
    
#     def __str__(self):
#         return f'PSM RAKERNIS - {self.satker.nama_satker}'

# class PSM_RAKERNIS(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(auto_now=True, editable=False)
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakernis_created_by")
#     updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakernis_updated_by")
#     satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_rakernis_satker", verbose_name="SATUAN KERJA PELAKSANA")
    
#     class Meta:
#         ordering = ['-updated_at']
#         verbose_name = 'PSM RAKERNIS'
#         verbose_name_plural = f'DAFTAR {verbose_name}'
#         db_table = 'kegiatan_psm_rakernis'
    
#     def __str__(self):
#         return f'PSM RAKERNIS - {self.satker.nama_satker}'

# class PSM_RAKERNIS(models.Model):
#     # foreign
#     id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="Rakernis_id_user")
#     # Fields
#     satker_pelaksana = models.CharField(max_length=30)
#     satker_bnnp_bnnk_diundang = models.CharField(max_length=30)
#     deskripsi_hasil = models.TextField(max_length=100)
#     rekomendasi = models.TextField(max_length=100)
#     hambatan_kendala = models.TextField(max_length=100)
#     tanggal = models.DateTimeField()
#     kesimpulan = models.TextField(max_length=100)
#     dokumentasi = models.FileField(upload_to="upload/files/psm/rakernis/")
#     created = models.DateTimeField(auto_now_add=True, editable=False)
#     last_updated = models.DateTimeField(auto_now=True, editable=False)

#     class Meta:
#         pass

#     def __str__(self):
#         return str(self.pk)