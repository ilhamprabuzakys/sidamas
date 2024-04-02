from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

from users.models import Satker

# ======= PSM RAKERNIS MODEL =======
class PSM_RAKERNIS(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakernis_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakernis_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_rakernis_satker", verbose_name="SATUAN KERJA PELAKSANA")
    satker_target = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_rakernis_satker_target", verbose_name="SATUAN KERJA TARGET")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/rakernis/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM RAKERNIS'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_rakernis'

# ======= PSM BINAAN TEKNIS MODEL =======
class PSM_BINAAN_TEKNIS(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_bintek_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_bintek_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_bintek_satker", verbose_name="SATUAN KERJA PELAKSANA")
    satker_target = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_bintek_satker_target", verbose_name="SATUAN KERJA TARGET")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/bintek/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM BINAAN TEKNIS'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_binaan_teknis'

# ======= PSM ASISTENSI MODEL =======
class PSM_ASISTENSI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_asistensi_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_asistensi_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_asistensi_satker", verbose_name="SATUAN KERJA")
    jumlah_kegiatan = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Kegiatan')
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    tanggal = models.DateField(verbose_name='Tanggal', blank=True, null=True, default=date.today)
    
    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta')
    stakeholder = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Stakeholder Yang Diasistensi Dalam Rangka Kotan')

    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/asistensi/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM ASISTENSI'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_asistensi'
    
    def __str__(self):
        return f'{self.satker.nama_satker} PSM ASISTENSI - {self.tanggal}'
    
# ======= PSM TES URINE DETEKSI DINI MODEL =======
class PSM_TES_URINE_DETEKSI_DINI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_test_urine_deteksi_dini_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_test_urine_deteksi_dini_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_test_urine_deteksi_dini_satker", verbose_name="SATUAN KERJA")
    satker_target = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_tes_urine_satker_target", verbose_name="SATUAN KERJA TARGET")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)

    nama_lingkungan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nama Lingkungan')
    hasil_tes_urine = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hasil Tes Urine')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/tes_urine_deteksi_dini/", blank=True)
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM TES URINE DETEKSI DINI'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_test_urine_deteksi_dini'
    
    def __str__(self):
        return f'{self.satker.nama_satker} PSM TES URINE DETEKSI DINI - {self.tanggal}'
    
class PSM_TES_URINE_DETEKSI_DINI_PESERTA(models.Model):
    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    ]

    HASIL_TEST_CHOICES = [
        ('P', 'Positif'),
        ('N', 'Negatif'),
    ]

    parent = models.ForeignKey(PSM_TES_URINE_DETEKSI_DINI, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    nama_peserta = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=15, choices=JENIS_KELAMIN_CHOICES)
    hasil_test = models.CharField(max_length=15, choices=HASIL_TEST_CHOICES)
    alamat = models.TextField(blank=True, null=True,)

# ======= PSM MONITORING DAN EVALUASI SUPERVISI KEGIATAN KOTAN MODEL =======
class PSM_MONITORING_DAN_EVALUASI_SUPERVISI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_monev_supervisi_kegiatan_kotan_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_monev_supervisi_kegiatan_kotan_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_monev_supervisi_kegiatan_kotan_satker", verbose_name="SATUAN KERJA")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)

    nama_lingkungan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nama Lingkungan Dan Satker')
    status_indeks = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Status Indeks Kemandirian Partisipasi')
    nilai_ikp = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nilai IKP')
    status_ikp = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Status')
    deskripsi_hasil = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    simpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Simpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/monev_supervisi_kegiatan_kotan/", blank=True)
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM MONITORING DAN EVALUASI SUPERVISI KEGIATAN KOTAN'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_monev_supervisi_kegiatan_kotan'
    
    def __str__(self):
        return f'{self.satker.nama_satker} PSM MONITORING DAN EVALUASI SUPERVISI KEGIATAN KOTAN - {self.tanggal_awal}'
    
class PSM_MONITORING_DAN_EVALUASI_SUPERVISI_PESERTA(models.Model):

    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    ]

    parent = models.ForeignKey(PSM_MONITORING_DAN_EVALUASI_SUPERVISI, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    nama_peserta = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=15, choices=JENIS_KELAMIN_CHOICES)
    jabatan = models.CharField(max_length=100, blank=True, null=True,)

# ======= PSM RAKOR PEMETAAN MODEL =======
class PSM_RAKOR_PEMETAAN(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakor_pemetaan_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_rakor_pemetaan_updated_by")
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_rakor_pemetaan_satker", verbose_name="SATUAN KERJA PELAKSANA")
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    nama_lingkungan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nama Lingkungan')  
    peserta = models.JSONField(blank=True, null=True, verbose_name='Data Peserta')
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/rakor_pemetaan/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
        
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM RAKOR PEMETAAN'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_rakor_pemetaan'
        
# ======= PSM AUDIENSI MODEL =======
class PSM_AUDIENSI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_audiensi_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="psm_audiensi_updated_by")
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="psm_audiensi_satker", verbose_name="SATUAN KERJA PELAKSANA")
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan', blank=True, null=True, default=date.today)
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True, default=date.today)
    nama_lingkungan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Nama Lingkungan')  
    peserta = models.JSONField(blank=True, null=True, verbose_name='Data Peserta')
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    dokumentasi = models.FileField(upload_to="uploads/kegiatan/psm/audiensi/")
    status = models.IntegerField(default=0, verbose_name="Status Pengiriman Kegiatan")
        
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'PSM AUDIENSI'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_psm_audiensi'