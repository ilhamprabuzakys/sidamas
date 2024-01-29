from datetime import datetime, time
import random
import string
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


"""
    Skema nya itu Tabel Data Survei memiliki foreignKey ke Tabel Tipe Survei
    Di Tipe Survei terdapat daftar_pertanyaan survei
    Kalo di Tabel Data Survei cuma sebagai tempat buat inisialisasi doang kayak waktu berlakunya survei mulai dari tanggal sampai jam berlakunya survei.
    
"""

# Percobaan
class TipeSurvei(models.Model):
    nama = models.CharField(max_length=255)
    daftar_pertanyaan = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="tipe_survei_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="tipe_survei_updated_by")
    
    class Meta:
        ordering = ['nama', ]
        verbose_name = 'Tipe Survei'
        verbose_name_plural = 'Daftar Tipe Survei'
        
    def __str__(self):
        return f'Tipe Survei - {self.nama}'

class DataSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_survei_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_survei_updated_by")
    
    dikirimkan_kepada = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="daftar_data_survei")
    
    judul = models.CharField(max_length=255, blank=True, null=True)
    
    tanggal = models.DateField(blank=True, null=True)
    
    jam_awal = models.TimeField(blank=True, null=True)
    jam_akhir = models.TimeField(blank=True, null=True)
    batas_responden = models.IntegerField(blank=True, null=True)
    
    status_pengiriman = models.BooleanField(blank=True, null=True, default=False)
    kode = models.CharField(max_length=255, blank=True, null=True, unique=True)
    
    # Relasi
    tipe = models.ForeignKey(TipeSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name='survei')

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Data Survei'
        verbose_name_plural = 'Daftar Data Survei'
        
    def generate_unique_code(self):
        # Menghasilkan kode acak
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        # Mengecek apakah kode sudah digunakan
        while DataSurvei.objects.filter(kode=random_string).exists():
            random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        return random_string
    
    def get_jumlah_responden(self):
        return self.responden.count()
    
    def save(self, *args, **kwargs):
        if not self.kode:
            self.kode = self.generate_unique_code()
        super().save(*args, **kwargs)
    
    def get_status_responden(self):
        if self.get_jumlah_responden() >= self.batas_responden:
            return 'Sudah penuh'
        else:
            return 'Belum penuh'
    
    def get_status_keberlangsungan(self):
        current_datetime = datetime.now()
        current_time = current_datetime.time()

        if self.tanggal > current_datetime.date() or (self.tanggal == current_datetime.date() and self.jam_awal > current_time):
            return 'Belum dibuka'
        elif self.tanggal == current_datetime.date() and self.jam_awal <= current_time < self.jam_akhir:
            return 'Berlangsung'
        elif self.tanggal < current_datetime.date() or (self.tanggal == current_datetime.date() and current_time >= self.jam_akhir):
            return 'Berakhir'
        else:
            return '?'
    
    def __str__(self):
        return f'Survei {self.tipe.nama} - {self.tanggal}'
    
class DataRespondenSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_responden_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_responden_updated_by")

    JENIS_KELAMIN_CHOICES = [
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    ]

    jenis_kelamin = models.CharField(max_length=15, choices=JENIS_KELAMIN_CHOICES)

    RENTANG_USIA_CHOICES = [
        ('12-25', '12 - 25 tahun'),
        ('26-45', '26 - 45 tahun'),
        ('46-65', '46 - 65 tahun'),
    ]
    
    rentang_usia = models.CharField(max_length=30, choices=RENTANG_USIA_CHOICES)
    
    PENDIDIKAN_CHOICES = [
        ('Doktor (S3)', 'Doktor (S3)'),
        ('Magister (S2)', 'Magister (S2)'),
        ('Sarjana (S1)', 'Sarjana (S1)'),
        ('Diploma (D1-D4)', 'Diploma (D1-D4)'),
        ('SMA/SMK/MA', 'SMA/SMK/MA'),
        ('SMP/MTs', 'SMP/MTs'),
    ]
    
    pendidikan = models.CharField(max_length=50, choices=PENDIDIKAN_CHOICES)
    
    # Bisi nanti diperlukan
    nama = models.CharField(blank=True, null=True, max_length=100)
    pekerjaan = models.CharField(blank=True, null=True, max_length=100)
    
    # Relasi
    survei = models.ForeignKey(DataSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="responden")
    
    class Meta:
        ordering = ['-updated_at', ]
        verbose_name = 'Data Responden Survei'
        verbose_name_plural = 'Daftar Data Responden Survei'

    def __str__(self):
        return str(self.pk)
    
class DataPengisianSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian_created_by")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian_updated_by")
    
    array_nilai_jawaban = models.TextField()
    data_mentahan = models.TextField()
    sigma_nilai = models.FloatField()
    
    # Relasi
    survei = models.ForeignKey(DataSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian")
    
    #responden = models.ForeignKey(DataRespondenSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian")
    
    responden = models.OneToOneField(DataRespondenSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name="data_pengisian")


    class Meta:
        ordering = ['-updated_at', ]
        verbose_name = 'Data Pengisian Survei'
        verbose_name_plural = 'Daftar Data Pengisian Survei'

    def __str__(self):
        return str(self.pk)