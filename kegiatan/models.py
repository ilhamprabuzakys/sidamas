from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# rakernis
class rakernis_psm(models.Model):
    # foreign
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="Rakernis_id_user")
    # Fields
    satker_pelaksana = models.CharField(max_length=30)
    satker_bnnp_bnnk_diundang = models.CharField(max_length=30)
    deskripsi_hasil = models.TextField(max_length=100)
    rekomendasi = models.TextField(max_length=100)
    hambatan_kendala = models.TextField(max_length=100)
    tanggal = models.DateTimeField()
    kesimpulan = models.TextField(max_length=100)
    dokumentasi = models.FileField(upload_to="upload/files/psm/rakernis/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)
#

# =============================================
# PSM
# =============================================

# =============================================
# DAYATIF
# =============================================