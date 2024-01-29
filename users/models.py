from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Satker(models.Model):
    nama_satker = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    level = models.IntegerField(default=1)
    
    class Meta:
        ordering = ['nama_satker', ]
        verbose_name = 'Satuan Kerja'
        verbose_name_plural = 'Daftar Satuan Kerja'
    
    def __str__(self):
        return str(self.nama_satker)
        
class Profile(models.Model):
    DIREKTOAT_CHOICES = (
        ('psm', 'PSM'),
        ('dayatif', 'Dayatif'),
    )
    
    satker = models.ForeignKey(Satker, on_delete=models.CASCADE, null=True, blank=True,)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(null=True, blank=True, max_length=12, choices=DIREKTOAT_CHOICES)
    is_verified = models.BooleanField(default=False)
    avatar = models.ImageField(
        default='images/avatar.png', # default avatar
        upload_to='profile_avatars' # dir to store the image
    )

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Profile User'
        verbose_name_plural = 'Daftar Profile User'
        
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)

class reg_provinces(models.Model):
    kode_provinsi = models.CharField(max_length=10)
    nama_provinsi = models.CharField(max_length=100)

    
    class Meta:
        ordering = ['nama_provinsi', ]
        verbose_name = 'Provinsi'
        verbose_name_plural = 'Daftar Provinsi'
        
    def __str__(self):
        return str(self.nama_provinsi)

class reg_regencies(models.Model):
    kode_kabupaten = models.CharField(max_length=10)
    kode_provinsi = models.ForeignKey('reg_provinces', on_delete=models.CASCADE, null=True, blank=True)
    nama_kabupaten = models.CharField(max_length=100)

    class Meta:
        ordering = ['nama_kabupaten', ]
        verbose_name = 'Kabupaten'
        verbose_name_plural = 'Daftar Kabupaten'
        
    def __str__(self):
        return str(self.nama_kabupaten)

class reg_district(models.Model):
    kode_kecamatan = models.CharField(max_length=10)
    kode_kabupaten = models.ForeignKey('reg_regencies', on_delete=models.CASCADE, null=True, blank=True)
    nama_kecamatan = models.CharField(max_length=100)

    class Meta:
        ordering = ['nama_kecamatan', ]
        verbose_name = 'Kecamatan'
        verbose_name_plural = 'Daftar Kecamatan'

    def __str__(self):
        return str(self.nama_kecamatan)

class reg_villages(models.Model):
    kode_desa = models.CharField(max_length=10)
    kode_kecamatan = models.ForeignKey('reg_district', on_delete=models.CASCADE, null=True, blank=True)
    nama_desa = models.CharField(max_length=100)

    class Meta:
        ordering = ['nama_desa', ]
        verbose_name = 'Desa'
        verbose_name_plural = 'Daftar Desa'
    
    def __str__(self):
        return str(self.nama_desa)

