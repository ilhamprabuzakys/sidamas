from datetime import datetime, time
import random
import string
from django.db import models
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
    
    class Meta:
        ordering = ['nama', ]
        verbose_name = 'Tipe Survei'
        verbose_name_plural = 'Daftar Tipe Survei'
        
    def __str__(self):
        return f'Tipe Survei - {self.nama}'

class DataSurvei(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    judul = models.CharField(max_length=255, blank=True, null=True)
    
    tanggal = models.DateField(blank=True, null=True)
    
    jam_awal = models.TimeField(blank=True, null=True)
    jam_akhir = models.TimeField(blank=True, null=True)
    jumlah_responden = models.IntegerField(blank=True, null=True)
    
    status_pengiriman = models.BooleanField(blank=True, null=True, default=False)
    kode = models.CharField(max_length=255, blank=True, null=True, unique=True)
    
    # Relasi
    tipe = models.ForeignKey(TipeSurvei, on_delete=models.CASCADE, blank=True, null=True, related_name='survei')

    class Meta:
        ordering = ['-tanggal', ]
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
        if self.get_jumlah_responden() >= self.jumlah_responden:
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


class tbl_responden_survei(models.Model):
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    pendidikan = models.CharField(max_length=30)
    jawaban = models.TextField()
    id_survei = models.IntegerField()
    nama = models.CharField(max_length=30)
    jenis_kelamin = models.CharField(max_length=30)
    perusahaan = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    pekerjaan = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("survei_tbl_responden_survei_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("survei_tbl_responden_survei_update", args=(self.pk,))


class tbl_survei(models.Model):
    # Fields
    tanggal = models.DateField()
    url = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    jam_awal = models.TimeField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    role = models.CharField(max_length=30)
    tipe = models.CharField(max_length=30)
    judul = models.CharField(max_length=30)
    status = models.BooleanField()
    jam_akhir = models.TimeField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("survei_tbl_survei_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("survei_tbl_survei_update", args=(self.pk,))


class tbl_data_responden(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    rentang_usia = models.CharField(max_length=30)
    pendidikan_terkahir = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    jenis_kelamin = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("survei_tbl_data_responden_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("survei_tbl_data_responden_update", args=(self.pk,))


class tbl_isi_survei(models.Model):
    # relasi
    id_data_survei = models.ForeignKey(
        "tbl_data_survei", on_delete=models.CASCADE, null=True
    )
    id_data_responden = models.ForeignKey(
        "tbl_data_responden", on_delete=models.CASCADE, null=True
    )
    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    array_nilai_jawaban = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    data_mentahan = models.TextField()
    sigma_nilai = models.FloatField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("survei_tbl_isi_survei_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("survei_tbl_isi_survei_update", args=(self.pk,))


# Tabel Utama Survei
class tbl_data_survei(models.Model):
    SKM_LIFE_SKILL = 'skm_life_skill'
    SKM_TES_URINE = 'skm_tes_urine'
    SKM = 'skm'

    SURVEY_TYPES = [
        (SKM_LIFE_SKILL, 'SKM Life Skill'),
        (SKM_TES_URINE, 'SKM Tes Urine'),
        (SKM, 'SKM'),
    ]

    nama = models.CharField(max_length=255)
    tipe = models.CharField(max_length=20, choices=SURVEY_TYPES)
    tanggal = models.DateField(blank=True, null=True)
    daftar_pertanyaan = models.JSONField()

    jam_awal = models.TimeField(blank=True, null=True)
    jam_akhir = models.TimeField(blank=True, null=True)
    jumlah_responden = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    kode = models.CharField(max_length=255, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama