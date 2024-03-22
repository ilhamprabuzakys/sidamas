from random import choices
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from users.models import Satker

# =============================================
# DAYATIF : 8
# =============================================

"""
    Setiap Kegiatan memiliki kolom status yang memiliki arti yakni Status Pengiriman, yang masing-masing nilai memiliki arti :
    0: Kegiatan belum dikirim ke manapun
    1: Kegiatan sudah dikirim ke BNNP
    2: Kegiatan sudah dikirim ke Pusat
"""

class DAYATIF_BINAAN_TEKNIS(models.Model):
    class STATUS_PENGIRIMAN_CHOICES(models.IntegerChoices):
        BELUM = 0
        BNNP = 1
        BNN_PUSAT = 2
        
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')
    # status = models.IntegerField(choices=STATUS_PENGIRIMAN_CHOICES, default=0, verbose_name='Status Pengiriman Kegiatan')
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_binaan_teknis_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_binaan_teknis_updated_by")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)
    
    jumlah_hari_pelaksanaan = models.IntegerField(default=2, verbose_name='Jumlah Hari Pelaksanaan Kegiatan')
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_binaan_teknis_satker", verbose_name="SATUAN KERJA PELAKSANA")
    
    satker_target = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, related_name="dayatif_binaan_teknis_satker_target", verbose_name="SATUAN KERJA TARGET")
    
    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta Kegiatan')
    
    tujuan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tujuan')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    
    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/binaan_teknis/')
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF KEGIATAN BINAAN TEKNIS'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_binaan_teknis'
    
    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF BINAAN TEKNIS - {self.tanggal_awal} s/d {self.tanggal_akhir} - Target : {self.satker_target.nama_satker}'

class DAYATIF_PEMETAAN_POTENSI(models.Model):
    status = models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan')
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_pemetaan_potensi_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_pemetaan_potensi_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_pemetaan_potensi_satker", verbose_name="SATUAN KERJA PELAKSANA")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)
    
    jumlah_hari_pelaksanaan = models.IntegerField(default=2, verbose_name='Jumlah Hari Pelaksanaan Kegiatan')
    
    desa = models.CharField(max_length=258, blank=True, null=True)
    kecamatan = models.CharField(max_length=258, blank=True, null=True)
    kabupaten = models.CharField(max_length=258, blank=True, null=True)
    provinsi = models.CharField(max_length=258, blank=True, null=True)
    
    nama_desa = models.CharField(max_length=150, blank=True, null=True)
    nama_kecamatan = models.CharField(max_length=150, blank=True, null=True)
    nama_kabupaten = models.CharField(max_length=150, blank=True, null=True)
    nama_provinsi = models.CharField(max_length=150, blank=True, null=True)
    
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    
    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/pemetaan_potensi/')
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF PEMETAAN POTENSI'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_pemetaan_potensi'
    
    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF PEMETAAN POTENSI - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_PEMETAAN_STAKEHOLDER(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_pemetaan_stakeholder_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_pemetaan_stakeholder_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_pemetaan_stakeholder_satker", verbose_name="SATUAN KERJA PELAKSANA")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)
    
    desa = models.IntegerField(blank=True, null=True)
    kecamatan = models.IntegerField(blank=True, null=True)
    kabupaten = models.IntegerField(blank=True, null=True)
    provinsi = models.IntegerField(blank=True, null=True)
    
    stakeholder = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Daftar Stakeholder')
    
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    
    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/pemetaan_stakeholder/')
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF PEMETAAN STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_pemetaan_stakeholder'
    
    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF PEMETAAN STAKEHOLDER - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_RAPAT_SINERGI_STAKEHOLDER(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_rapat_sinergi_stakeholder_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_rapat_sinergi_stakeholder_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_rapat_sinergi_stakeholder_satker", verbose_name="SATUAN KERJA PELAKSANA")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan', blank=True, null=True)
    
    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta Kegiatan')
    
    desa = models.IntegerField(blank=True, null=True)
    kecamatan = models.IntegerField(blank=True, null=True)
    kabupaten = models.IntegerField(blank=True, null=True)
    provinsi = models.IntegerField(blank=True, null=True)
    
    stakeholder = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Daftar Stakeholder Pendamping')
    
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    rekomendasi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Rekomendasi')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    
    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/rapat_sinergi_stakeholder/')
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF RAPAT SINERGI STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_rapat_sinergi_stakeholder'
    
    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF RAPAT SINERGI STAKEHOLDER - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_BIMBINGAN_TEKNIS_STAKEHOLDER(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_bimbingan_teknis_stakeholder_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_bimbingan_teknis_stakeholder_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_bimbingan_teknis_stakeholder_satker", verbose_name="SATUAN KERJA PELAKSANA")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan')
    
    JENIS_BIMBINGAN_CHOICES = (
        ('bimbingan_teknis_stakeholder', 'Bimbingan Teknis Stakeholder'),
        ('bimbingan_teknis_pendamping', 'Bimbingan Teknis Pendamping')
	)
    
    jenis_bimbingan = models.CharField(max_length=max(len(key) for key, _ in JENIS_BIMBINGAN_CHOICES), choices=JENIS_BIMBINGAN_CHOICES, default="bimbingan_teknis_stakeholder", verbose_name='Jenis Bimbingan')
    
    tempat = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tempat')
    jumlah_peserta = models.IntegerField(blank=True, null=True, verbose_name='Jumlah Peserta Yang Hadir')
    
    stakeholder = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Daftar Stakeholder Pendamping')
    
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    rekomendasi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Rekomendasi')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    
    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/bimbingan_teknis_stakeholder/')
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF BIMBINGAN TEKNIS STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_bimbingan_teknis_stakeholder'
    
    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF BIMBINGAN TEKNIS STAKEHOLDER - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_bimbingan_teknis_lifeskill_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_bimbingan_teknis_lifeskill_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_bimbingan_teknis_lifeskill_satker", verbose_name="SATUAN KERJA PELAKSANA")
    
    tanggal_awal = models.DateField(verbose_name='Tanggal Awal Kegiatan')
    tanggal_akhir = models.DateField(verbose_name='Tanggal Akhir Kegiatan')
    
    tempat = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tempat')
    
    # Kawasan yang diintervensi
    desa = models.IntegerField(blank=True, null=True)
    kecamatan = models.IntegerField(blank=True, null=True)
    kabupaten = models.IntegerField(blank=True, null=True)
    provinsi = models.IntegerField(blank=True, null=True)
    
    KETERAMPILAN_CHOICES = (
        ('menjahit', 'Menjahit'),
        ('kerajinan_tangan', 'Kerajinan Tangan'),
        ('pengolahan_makanan', 'Pengolahan Makanan'),
        ('pembuatan_sabun', 'Pembuatan Sabun'),
        ('barista_kopi', 'Barista Kopi'),
        ('lainnya', 'Lainnya')
	)
    
    keterampilan = models.CharField(max_length=max(len(key) for key, _ in KETERAMPILAN_CHOICES), choices=KETERAMPILAN_CHOICES, default="menjahit", verbose_name='Jenis Bimbingan')
    
    keterampilan_detail = models.CharField(max_length=100, blank=True, null=True)
    
    sinergi_desa = models.BooleanField(default=False, verbose_name='Sinergi Desa')
    sinergi_ibm = models.BooleanField(default=False, verbose_name='Sinergi IBM')
    
    hasil_skm_nilai = models.FloatField(blank=True, null=True, verbose_name='Hasil SKM Nilai')
    
    HASIL_SKM_KATEGORI_CHOICES = (
        ('buruk', 'Buruk'),
        ('cukup', 'Cukup'),
        ('baik', 'Baik'),
        ('sangat_baik', 'Sangat Baik')
	)
    
    hasil_skm_kategori = models.CharField(max_length=max(len(key) for key, _ in HASIL_SKM_KATEGORI_CHOICES), choices=HASIL_SKM_KATEGORI_CHOICES, default="cukup", verbose_name='Hasil SKM Kategori')
    
    deskripsi = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Deskripsi Hasil')
    kendala = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Hambatan/Kendala')
    kesimpulan = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Kesimpulan')
    tindak_lanjut = models.TextField(blank=True, null=True, max_length=2000, verbose_name='Tindak Lanjut')
    
    dokumentasi = models.FileField(upload_to='uploads/kegiatan/dayatif/bimbingan_teknis_lifeskill/')
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF BIMBINGAN TEKNIS LIFESKILL'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_bimbingan_teknis_lifeskill'
    
    def __str__(self):
        return f'{self.satker.nama_satker} DAYATIF BIMBINGAN TEKNIS LIFESKILL - {self.tanggal_awal} s/d {self.tanggal_akhir}'

class DAYATIF_BIMBINGAN_TEKNIS_LIFESKILL_PESERTA(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    nama = models.CharField(max_length=100, blank=True, null=True)
    alamat = models.TextField(max_length=1000, blank=True, null=True)
    no_telepon = models.CharField(max_length=18, blank=True, null=True)
    
    JENIS_KELAMIN_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
	)
    
    jenis_kelamin = models.CharField(max_length=1, choices=JENIS_KELAMIN_CHOICES, default="L", verbose_name='Jenis Kelamin')
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF PESERTA BIMBINGAN TEKNIS LIFESKILL'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_bimbingan_teknis_lifeskill_peserta'
    
    def __str__(self):
        return f'{self.nama} DAYATIF PESERTA BIMBINGAN TEKNIS LIFESKILL'

class DAYATIF_MONITORING_DAN_EVALUASI(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_monitoring_dan_evaluasi_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_monitoring_dan_evaluasi_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_monitoring_dan_evaluasi_satker", verbose_name="SATUAN KERJA PELAKSANA")
    
    JENIS_CHOICES = (
        ('monitoring_dan_evaluasi_kerja', 'Monitoring dan Evaluasi Kerja'),
        ('monitoring_dan_evaluasi_dalam_rangka_pendampingan', 'Monitoring dan Evaluasi dalam rangka pendampingan')
	)
    
    PERIODE_CHOICES = (
		('triwulan', 'Triwulan'),
		('semester', 'Semester'),
		('tahunan', 'Tahunan')
	)
    
    jenis = models.CharField(max_length=50, choices=JENIS_CHOICES, default="monitoring_dan_evaluasi_kerja")
    periode = models.CharField(max_length=10, choices=PERIODE_CHOICES, default="triwulan")
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF MONITORING DAN EVALUASI'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_monitoring_dan_evaluasi'
    
    def __str__(self):
        return f'DAYATIF MONITORING DAN EVALUASI - {self.satker.nama_satker}'

class DAYATIF_DUKUNGAN_STAKEHOLDER(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_dukungan_stakeholder_created_by")
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="dayatif_dukungan_stakeholder_updated_by")
    
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, blank=True, null=True, related_name="dayatif_dukungan_stakeholder_satker", verbose_name="SATUAN KERJA PELAKSANA")
    
    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'DAYATIF DUKUNGAN STAKEHOLDER'
        verbose_name_plural = f'DAFTAR {verbose_name}'
        db_table = 'kegiatan_dayatif_dukungan_stakeholder'
    
    def __str__(self):
        return f'DAYATIF DUKUNGAN STAKEHOLDER - {self.satker.nama_satker}'