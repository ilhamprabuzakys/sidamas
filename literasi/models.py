from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Literasi(models.Model):
    STATUS_CHOICES = (
        ('1', 'DRAFT'),
        ('2', 'PUBLISH'),
        ('3', 'ARCHIVE'),
    )
    KATEGORI_CHOICES = (
        ('1', 'Petunjuk Kerja'),
        ('2', 'e-Book'),
        ('3', 'Bahan Sosialisasi'),
        ('4', 'Materi Pelatihan'),
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="Literasi_updated_by")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="Literasi_created_by")
    
    dokumen = models.FileField(upload_to="upload/files/literasi")
    Judul = models.TextField(max_length=1000)
    tags = models.TextField(max_length=1000)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="1")
    kategori = models.CharField(max_length=1, choices=KATEGORI_CHOICES, default="1")
    
    class Meta:
        ordering = ['-updated_at', ]
        verbose_name = 'Literasi'
        verbose_name_plural = 'Daftar Literasi'

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("literasi_literasi_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("literasi_literasi_update", args=(self.pk,))

