# Generated by Django 3.2.24 on 2024-03-21 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kegiatan', '0012_psm_tes_urine_deteksi_dini_psm_tes_urine_deteksi_dini_peserta'),
    ]

    operations = [
        migrations.AddField(
            model_name='psm_tes_urine_deteksi_dini_peserta',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kegiatan.psm_tes_urine_deteksi_dini'),
        ),
    ]
