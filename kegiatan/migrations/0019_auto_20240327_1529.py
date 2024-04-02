# Generated by Django 3.2.24 on 2024-03-27 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0018_alter_psm_tes_urine_deteksi_dini_dokumentasi'),
    ]

    operations = [
        migrations.AddField(
            model_name='psm_asistensi',
            name='status',
            field=models.IntegerField(default=0, verbose_name='Status Pengiriman Kegiatan'),
        ),
        migrations.AddField(
            model_name='psm_asistensi',
            name='tanggal_akhir',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Tanggal Akhir Kegiatan'),
        ),
        migrations.AddField(
            model_name='psm_asistensi',
            name='tanggal_awal',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Tanggal Awal Kegiatan'),
        ),
    ]