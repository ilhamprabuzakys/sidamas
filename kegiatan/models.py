from django.db import models
from django.urls import reverse

# rakernis
class tbl_rakernis_psm(models.Model):
    # foreign
    id_user = models.IntegerField()
    # Fields
    satuan_kerja_pelaksana_kegiatan = models.CharField(max_length=30)
    satker_bnnp_bnnk_diundang = models.CharField(max_length=30)
    deskripsi_hasil = models.TextField(max_length=100)
    rekomendasi = models.TextField(max_length=100)
    hambatan_kendala = models.TextField(max_length=100)
    tanggal = models.DateTimeField()
    simpulan = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/psm/rakernis/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_rakernis_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_rakernis_psm_update", args=(self.pk,))
# 

# bimtek
class tbl_bimtek_psm(models.Model):

    #relasi 
    id_user = models.IntegerField()
    # Fields
    deskripsi_hasil = models.TextField(max_length=100)
    tanggal = models.DateTimeField()
    jumlah_kegiatan = models.IntegerField()
    satker_dibimtek = models.CharField(max_length=30)
    rekomendasi = models.TextField(max_length=100)
    satuan_kerja_pelaksana_kegiatan = models.CharField(max_length=30)
    tindak_lanjut = models.TextField(max_length=100)
    no = models.IntegerField()
    simpulan = models.TextField(max_length=100)
    hambatan_kendala = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/psm/bimtek/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_bimtek_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_bimtek_psm_update", args=(self.pk,))
# 

# rakor pemetaan
class tbl_rakor_pemetaan_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja_pelaksana_kegiatan = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_rakor_pemetaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_rakor_pemetaan_psm_update", args=(self.pk,))

class tbl_rakor_pemetaan_pelaksanaan_psm(models.Model):

    # relasi
    id_tbl_rakor_pemetaan_psm = models.ForeignKey("tbl_rakor_pemetaan_psm", on_delete=models.CASCADE, null=True)

    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    peserta = models.CharField(max_length=30)
    sasaran_lingkungan = models.CharField(max_length=30)
    deskripsi_hasil = models.TextField(max_length=100)
    hambatan_kendala = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.CharField(max_length=30)
    file = models.FileField(upload_to="upload/files/psm/rakor_pemetaan/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_rakor_pemetaan_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_rakor_pemetaan_pelaksanaan_psm_update", args=(self.pk,))
# 

# audiensi
class tbl_audiensi_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja_pelaksana_kegiatan = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_audiensi_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_audiensi_psm_update", args=(self.pk,))

class tbl_audiensi_pelaksanaan_psm(models.Model):

    #relasi 
    id_tbl_audiensi_psm = models.ForeignKey("tbl_audiensi_psm", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    peserta = models.CharField(max_length=30)
    sasaran_lingkungan = models.TextField(max_length=100)
    deskripsi_hasil = models.TextField(max_length=100)
    hambatan_kendala = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.CharField(max_length=30)
    file = models.FileField(upload_to="upload/files/psm/audiensi/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_audiensi_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_audiensi_pelaksanaan_psm_update", args=(self.pk,))
# 

# konsolidasi kebijakan
class tbl_konsolidasi_kebijakan_psm(models.Model):

    # relasi
    id_user = models.IntegerField()

    # Fields
    satuan_kerja_pelaksana_kegiatan = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_konsolidasi_kebijakan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_konsolidasi_kebijakan_psm_update", args=(self.pk,))

class tbl_konsolidasi_kebijakan_pelaksanaan_psm(models.Model):

    #relasi
    id_tbl_konsolidasi_kebijakan_psm = models.ForeignKey("tbl_konsolidasi_kebijakan_psm", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    peserta = models.CharField(max_length=30)
    stakeholde_pendamping_yang_diundang = models.CharField(max_length=30)
    deskripsi_hasil = models.TextField(max_length=100)
    hambatan_kendala = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/psm/konsolidasi_kebijakan/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_konsolidasi_kebijakan_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_konsolidasi_kebijakan_pelaksanaan_psm_update", args=(self.pk,))
# 

# workshop penggiat
class tbl_workshop_penggiat_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja_pelaksana_kegiatan = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_workshop_penggiat_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_workshop_penggiat_psm_update", args=(self.pk,))

class tbl_workshop_penggiat_pelaksanaan_psm(models.Model):
    
    #relasi 
    id_tbl_workshop_penggiat_psm = models.ForeignKey("tbl_workshop_penggiat_psm", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    peserta = models.CharField(max_length=30)
    stakeholde_pendamping_yang_diundang = models.CharField(max_length=30)
    deskripsi_hasil = models.TextField(max_length=100)
    hambatan_kendala = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.CharField(max_length=30)
    file = models.FileField(upload_to="upload/files/psm/workshop/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_workshop_penggiat_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_workshop_penggiat_pelaksanaan_psm_update", args=(self.pk,))
# 

# bimtek penggiat P4GN
class tbl_bimtek_penggiat_p4gn_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja_pelaksana_kegiatan = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_bimtek_penggiat_p4gn_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_bimtek_penggiat_p4gn_psm_update", args=(self.pk,))

class tbl_bimtek_penggiat_p4gn_lingkungan_psm(models.Model):

    #relasi 
    id_tbl_bimtek_penggiat_p4gn_psm = models.ForeignKey("tbl_bimtek_penggiat_p4gn_psm", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    nama_lingkungan = models.CharField(max_length=30)
    no_seri_pin_penggiat = models.IntegerField()
    nama = models.CharField(max_length=30)
    jabatan = models.CharField(max_length=30)
    jenis_kelamin = models.CharField(max_length=30)
    jumlah_peserta = models.IntegerField()
    daftar_nama_peserta = models.IntegerField()
    hasil_capaian = models.CharField(max_length=30)
    kesimpulan = models.CharField(max_length=30)
    tindak_lanjut = models.CharField(max_length=30)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_bimtek_penggiat_p4gn_lingkungan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_bimtek_penggiat_p4gn_lingkungan_psm_update", args=(self.pk,))
# 

# sinkronisasi kebijakan
class tbl_sinkronisasi_kebijakan_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_sinkronisasi_kebijakan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_sinkronisasi_kebijakan_psm_update", args=(self.pk,))

class tbl_sinkronisasi_kebijakan_pelaksanaan_psm(models.Model):

    # relasi
    id_tbl_sinkronisasi_kebijakan_psm = models.ForeignKey("tbl_sinkronisasi_kebijakan_psm", on_delete=models.CASCADE, null=True)

    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    jumlah_peserta = models.IntegerField()
    stakeholder_yang_diundang = models.TextField(max_length=100)
    deskripsi_hasil = models.TextField(max_length=100)
    kendala_hambatan = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.CharField(max_length=30)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_sinkronisasi_kebijakan_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_sinkronisasi_kebijakan_pelaksanaan_psm_update", args=(self.pk,))
# 

# workshop tematik
class tbl_workshop_tematik_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_workshop_tematik_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_workshop_tematik_psm_update", args=(self.pk,))

class tbl_workshop_tematik_pelaksanaan_psm(models.Model):

    #relasi 
    id_tbl_workshop_tematik = models.ForeignKey("tbl_workshop_tematik_psm", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    jumlah_peserta = models.IntegerField()
    stakeholder_yang_diundang = models.TextField(max_length=100)
    deskripsi_hasil = models.TextField(max_length=100)
    kendala_hambatan = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_workshop_tematik_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_workshop_tematik_pelaksanaan_psm_update", args=(self.pk,))
# 

# asistensi
class tbl_asistensi_psm(models.Model):

    #relasi 
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_asistensi_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_asistensi_psm_update", args=(self.pk,))

class tbl_asistensi_pelaksanaan_psm(models.Model):

    #relasi 
    id_tbl_asistensi_psm = models.ForeignKey("tbl_asistensi_psm", on_delete=models.CASCADE, null=True)

    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    jumlah_peserta = models.IntegerField()
    stakeholde_yang_diasistensi_dalam_rangka_kotan = models.TextField(max_length=100)
    deskripsi_hasil = models.TextField(max_length=100)
    kendala_hambatan = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_asistensi_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_asistensi_pelaksanaan_psm_update", args=(self.pk,))
# 

#tes urine 
class tbl_tes_urine_deteksi_dini_psm(models.Model):
    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.TextField(max_length=100)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_tes_urine_deteksi_dini_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_tes_urine_deteksi_dini_psm_update", args=(self.pk,))

class tbl_tes_urine_deteksi_dini_pelaksanaan_psm(models.Model):

    #relasi 
    id_tbl_tes_urine_deteksi_dini_psm = models.ForeignKey("tbl_tes_urine_deteksi_dini_psm", on_delete=models.CASCADE, null=True)

    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    nama_lingkungan = models.TextField(max_length=100)
    jenis_kelamin = models.CharField(max_length=30)
    jumlah_peserta = models.IntegerField()
    nama = models.CharField(max_length=30)
    hasil_tes_urine = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_tes_urine_deteksi_dini_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_tes_urine_deteksi_dini_pelaksanaan_psm_update", args=(self.pk,))
# 

# monev supervisi kegiatan kotan
class tbl_monev_supervisi_kegiatan_kotan_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.TextField(max_length=100)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_monev_supervisi_kegiatan_kotan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_monev_supervisi_kegiatan_kotan_psm_update", args=(self.pk,))

class tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm(models.Model):

    #relasi 
    id_tbl_monev_supervisi_kegiatan_kotan_psm = models.ForeignKey("tbl_monev_supervisi_kegiatan_kotan_psm", on_delete=models.CASCADE, null=True)

    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    nama_lingkungan_dan_satker = models.TextField(max_length=100)
    nama_jabatan = models.CharField(max_length=30)
    jenis_kelamin = models.CharField(max_length=30)
    jumlah_peserta = models.IntegerField()
    status_indeks_kemandirian_partisipasi = models.CharField(max_length=30)
    nilai_skp = models.IntegerField()
    status = models.CharField(max_length=30)
    deskripsi_hasil = models.TextField(max_length=100)
    simpulan = models.TextField(max_length=100)
    tidak_lanjut = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_monev_supervisi_kegiatan_kotan_pelaksanaan_psm_update", args=(self.pk,))
# 

# pengumpulan data ikotan
class tbl_pengumpulan_data_ikotan_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    unit_observasi = models.TextField(max_length=100)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_pengumpulan_data_ikotan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_pengumpulan_data_ikotan_psm_update", args=(self.pk,))

class tbl_pengumpulan_data_ikotan_pelaksanaan_psm(models.Model):

    #relasi 
    id_tbl_pengumpulan_data_ikotan_pelaksanaan_psm = models.ForeignKey("tbl_pengumpulan_data_ikotan_pelaksanaan_psm", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    nama_responden = models.CharField(max_length=30)
    deskripsi_hasil = models.TextField(max_length=100)
    simpulan = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_pengumpulan_data_ikotan_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_pengumpulan_data_ikotan_pelaksanaan_psm_update", args=(self.pk,))
# 

# data dukungan stakeholder
class tbl_data_dukungan_stakeholder_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_data_dukungan_stakeholder_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_data_dukungan_stakeholder_psm_update", args=(self.pk,))
    
class tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm(models.Model):

    #relasi 
    id_tbl_pengumpulan_data_ikotan_pelaksanaan_psm = models.ForeignKey("tbl_pengumpulan_data_ikotan_pelaksanaan_psm", on_delete=models.CASCADE, null=True)
    # Fields
    nama_stakeholder = models.CharField(max_length=30)
    kegiatan_yang_dilakukan = models.TextField(max_length=100)
    nasional = models.CharField(max_length=30)
    provinsi = models.CharField(max_length=30)
    kota_kabupaten = models.CharField(max_length=30)
    kecamatan = models.CharField(max_length=30)
    kelurahan_desa = models.CharField(max_length=30)
    linkungan = models.CharField(max_length=30)
    jumlah_sasaran = models.IntegerField()
    hasil_dampak = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_data_dukungan_stakeholder_lingkup_kegiatan_p4gn_psm_update", args=(self.pk,))
# 

# kegiatan lainnya
class tbl_kegiatan_lainnya_psm(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_kegiatan_lainnya_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_kegiatan_lainnya_psm_update", args=(self.pk,))

class tbl_kegiatan_lainnya_pelaksanaan_psm(models.Model):

    #relasi 
    id_tbl_kegiatan_lainnya_psm = models.ForeignKey("tbl_kegiatan_lainnya_psm", on_delete=models.CASCADE, null=True)
    # Fields
    nama_kegiatan = models.CharField(max_length=30)
    tempat = models.CharField(max_length=30)
    waktu = models.TimeField()
    lingkungan_sasaran = models.CharField(max_length=30)
    jumlah_orang = models.IntegerField()
    hasil_dampak = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_kegiatan_lainnya_pelaksanaan_psm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_kegiatan_lainnya_pelaksanaan_psm_update", args=(self.pk,))
# 

# rekapitulasi pembinaan teknis ke bnnk
class tbl_rekapitulasi_pembinaan_teknis_dayatif(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_rekapitulasi_pembinaan_teknis_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_rekapitulasi_pembinaan_teknis_dayatif_update", args=(self.pk,))

class tbl_rekapitulasi_pembinaan_teknis_detail_dayatif(models.Model):

    #relasi 
    id_tbl_rekapitulasi_pembinaan_teknis_dayatif = models.ForeignKey("tbl_rekapitulasi_pembinaan_teknis_dayatif", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    satker_yang_dibimtek = models.CharField(max_length=30)
    hambatan_kendala = models.TextField(max_length=100)
    deskripsi_hasil = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    simpulan = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/dayatif/rekapitulasi_pembinaan_teknis_dayatif/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_rekapitulasi_pembinaan_teknis_detail_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_rekapitulasi_pembinaan_teknis_detail_dayatif_update", args=(self.pk,))
# 

# pemetaan potensi sdm dan sda kawasan rawan narkoba
class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif_update", args=(self.pk,))

class tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif(models.Model):

    #relasi 
    id_tbl_pemetaan_potensi_detail = models.ForeignKey("tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_dayatif", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    lokasi = models.TextField(max_length=100)
    deskripsi_hasil = models.TextField(max_length=100)
    kendala_hambatan = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    tindak_lanjut = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_pemetaan_potensi_sdm_dan_sda_kawasan_rawan_narkoba_detail_dayatif_update", args=(self.pk,))
# 

# pemetaan stakeholder pada kawasan rawan narkoba 
class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    satuan_kerja = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif_update", args=(self.pk,))

class tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif(models.Model):

    #relasi 
    id_tbl_pemetaan_stakeholder_detail = models.ForeignKey("tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_dayatif", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    lokasi = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    tanggal = models.DateField()
    kendala_hambatan = models.TextField(max_length=100)
    deskripsi_hasil = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_pemetaan_stakeholder_pada_kawasan_rawan_narkoba_detail_dayatif_update", args=(self.pk,))
# 

# rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholders
class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif_update", args=(self.pk,))

class tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif(models.Model):

    #relasi 
    id_tbl_rekapitulasi_kegiatan_detail = models.ForeignKey("tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_dayatif", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    jumlah_peserta = models.IntegerField()
    stakeholder_pendamping_yang_diundang = models.TextField(max_length=100)
    deskripsi_hasil = models.TextField(max_length=100)
    kendala_hambatan = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    tindak_lanjut = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_rekapitulasi_kegiatan_rapat_kerja_sinergi_stakeholder_detail_dayatif_update", args=(self.pk,))
# 

# kegiatan bimtek stakeholder/pendamping
class tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    satuan_kerja = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif_update", args=(self.pk,))

class tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif(models.Model):

    #relasi 
    id_tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif = models.ForeignKey("tbl_kegiatan_bimtek_stakeholder_pendamping_dayatif", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    tanggal = models.DateField()
    tindak_lanjut = models.TextField(max_length=100)
    jumlah_peserta = models.IntegerField()
    stakeholder_pendamping_yang_diundang = models.TextField(max_length=100)
    deskripsi_hasil = models.TextField(max_length=100)
    kendala_hambatan = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_kegiatan_bimtek_stakeholder_pendamping_detail_dayatif_update", args=(self.pk,))
# 

# bimbingan teknis life skill
class tbl_bimbingan_teknis_life_skill_dayatif(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    jumlah_kegiatan = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_bimbingan_teknis_life_skill_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_bimbingan_teknis_life_skill_dayatif_update", args=(self.pk,))

class tbl_bimbingan_teknis_life_skill_detail_dayatif(models.Model):

    #relasi 
    id_tbl_bimbingan_teknis_life_skill_dayatif = models.ForeignKey("tbl_bimbingan_teknis_life_skill_dayatif", on_delete=models.CASCADE, null=True)
    # Fields
    no = models.IntegerField()
    nilai = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    tindak_lanjut = models.TextField(max_length=100)
    kesimpulan = models.TextField(max_length=100)
    desa_bersinar = models.CharField(max_length=30)
    nama_kawasan = models.CharField(max_length=30)
    tanggal = models.DateField()
    kategori = models.IntegerField()
    nama_peserta = models.TextField(max_length=100)
    IBM = models.CharField(max_length=30)
    file = models.FileField(upload_to="upload/files/")
    jumlah_peserta = models.IntegerField()
    pria = models.IntegerField()
    wanita = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_bimbingan_teknis_life_skill_detail_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_bimbingan_teknis_life_skill_detail_dayatif_update", args=(self.pk,))
# 

# monev pemberdayaan alternatif kawasan rawan narkoba
class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    jumlah_kegiatan = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif_update", args=(self.pk,))

class tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif(models.Model):

    #relasi 
    id_tbl_monev_pemberdayaan_detail = models.ForeignKey("tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_dayatif", on_delete=models.CASCADE, null=True)
    # Fields
    nilai = models.IntegerField()
    deskripsi_hasil = models.TextField(max_length=100)
    ibm = models.CharField(max_length=30)
    tanggal = models.DateField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    jenis_pelatihan = models.CharField(max_length=30)
    simpulan = models.TextField(max_length=100)
    kategori = models.FloatField()
    file = models.FileField(upload_to="upload/files/")
    nama_kawasan = models.TextField(max_length=100)
    wanita = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    jumlah_peserta = models.IntegerField()
    tindak_lanjut = models.TextField(max_length=100)
    no = models.IntegerField()
    daftar_nama_peserta = models.CharField(max_length=30)
    desa_bersinar = models.CharField(max_length=30)
    pria = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_monev_pemberdayaan_alternatif_kawasan_rawan_narkoba_detail_dayatif_update", args=(self.pk,))
# 

# Monev dalam rangka pendampingan
class tbl_monev_rangka_pendampingan_masyarakat_dayatif(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    satuan_kerja = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    jumlah_kegiatan = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_monev_rangka_pendampingan_masyarakat_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_monev_rangka_pendampingan_masyarakat_dayatif_update", args=(self.pk,))

class tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif(models.Model):

    #relasi 
    id_tbl_monev_rangka_pendampingan_masyarakat_dayatif = models.ForeignKey("tbl_monev_rangka_pendampingan_masyarakat_dayatif", on_delete=models.CASCADE, null=True)
    # Fields
    simpulan = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    tindak_lanjut = models.TextField(max_length=100)
    no = models.IntegerField()
    deskripsi_hasil = models.TextField(max_length=100)
    tanggal = models.DateField()
    file = models.FileField(upload_to="upload/files/")
    lokasi = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_monev_rangka_pendampingan_masyarakat_detail_dayatif_update", args=(self.pk,))
# 

# 
class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif(models.Model):

    # relasi
    id_user = models.IntegerField()
    # Fields
    satuan_kerja = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_dayatif_update", args=(self.pk,))

class tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif(models.Model):

    #relasi 
    id_tbl_monev_rangka_pendampingan_masyarakat_dayatif = models.ForeignKey("tbl_monev_rangka_pendampingan_masyarakat_dayatif", on_delete=models.CASCADE, null=True)
    # Fields
    kesimpulan = models.TextField(max_length=100)
    kegiatan_yang_dilakukan = models.TextField(max_length=100)
    tindak_lanjut = models.CharField(max_length=30)
    file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    jumlah_sasaran = models.IntegerField()
    desa_kelurahan = models.CharField(max_length=30)
    kota_kabupaten = models.CharField(max_length=30)
    kecamatan = models.CharField(max_length=30)
    nama_stakeholder = models.CharField(max_length=30)
    hasil_dampak = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("pelaporan_tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("pelaporan_tbl_dukungan_stakeholder_dalam_pemberdayaan_alternatif_detail_dayatif_update", args=(self.pk,))
# 