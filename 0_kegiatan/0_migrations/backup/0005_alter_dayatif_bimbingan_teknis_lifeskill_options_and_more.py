# Generated by Django 4.1.7 on 2024-03-17 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0011_auto_20240221_1717'),
        ('kegiatan', '0004_dayatif_bimbingan_teknis_lifeskill_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dayatif_bimbingan_teknis_lifeskill',
            options={'ordering': ['-updated_at'], 'verbose_name': 'DAYATIF BIMBINGAN TEKNIS LIFESKILL', 'verbose_name_plural': 'DAFTAR DAYATIF BIMBINGAN TEKNIS LIFESKILL'},
        ),
        migrations.AlterModelOptions(
            name='dayatif_bimbingan_teknis_stakeholder',
            options={'ordering': ['-updated_at'], 'verbose_name': 'DAYATIF BIMBINGAN TEKNIS STAKEHOLDER', 'verbose_name_plural': 'DAFTAR DAYATIF BIMBINGAN TEKNIS STAKEHOLDER'},
        ),
        migrations.AlterModelOptions(
            name='dayatif_dukungan_stakeholder',
            options={'ordering': ['-updated_at'], 'verbose_name': 'DAYATIF DUKUNGAN STAKEHOLDER', 'verbose_name_plural': 'DAFTAR DAYATIF DUKUNGAN STAKEHOLDER'},
        ),
        migrations.AlterModelOptions(
            name='dayatif_monitoring_dan_evaluasi',
            options={'ordering': ['-updated_at'], 'verbose_name': 'DAYATIF MONITORING DAN EVALUASI', 'verbose_name_plural': 'DAFTAR DAYATIF MONITORING DAN EVALUASI'},
        ),
        migrations.AlterModelOptions(
            name='dayatif_pemetaan_potensi',
            options={'ordering': ['-updated_at'], 'verbose_name': 'DAYATIF PEMETAAN POTENSI', 'verbose_name_plural': 'DAFTAR DAYATIF PEMETAAN POTENSI'},
        ),
        migrations.AlterModelOptions(
            name='dayatif_pemetaan_stakeholder',
            options={'ordering': ['-updated_at'], 'verbose_name': 'DAYATIF PEMETAAN STAKEHOLDER', 'verbose_name_plural': 'DAFTAR DAYATIF PEMETAAN STAKEHOLDER'},
        ),
        migrations.AlterModelOptions(
            name='dayatif_rapat_sinergi_stakeholder',
            options={'ordering': ['-updated_at'], 'verbose_name': 'DAYATIF RAPAT SINERGI STAKEHOLDER', 'verbose_name_plural': 'DAFTAR DAYATIF RAPAT SINERGI STAKEHOLDER'},
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_lifeskill',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_lifeskill',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_bimbingan_teknis_lifeskill_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_lifeskill',
            name='satker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dayatif_bimbingan_teknis_lifeskill_satker', to='users.satker', verbose_name='SATUAN KERJA PELAKSANA'),
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_lifeskill',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_lifeskill',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_bimbingan_teknis_lifeskill_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_stakeholder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_stakeholder',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_bimbingan_teknis_stakeholder_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_stakeholder',
            name='jenis',
            field=models.CharField(choices=[('bimbingan_teknis_stakeholder', 'Bimbingan Teknis Stakeholder'), ('bimbingan_teknis_pendamping', 'Bimbingan Teknis Pendamping')], default='bimbingan_teknis_stakeholder', max_length=28),
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_stakeholder',
            name='satker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dayatif_bimbingan_teknis_stakeholder_satker', to='users.satker', verbose_name='SATUAN KERJA PELAKSANA'),
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_stakeholder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dayatif_bimbingan_teknis_stakeholder',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_bimbingan_teknis_stakeholder_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_dukungan_stakeholder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayatif_dukungan_stakeholder',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_dukungan_stakeholder_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_dukungan_stakeholder',
            name='satker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dayatif_dukungan_stakeholder_satker', to='users.satker', verbose_name='SATUAN KERJA PELAKSANA'),
        ),
        migrations.AddField(
            model_name='dayatif_dukungan_stakeholder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dayatif_dukungan_stakeholder',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_dukungan_stakeholder_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_monitoring_dan_evaluasi',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayatif_monitoring_dan_evaluasi',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_monitoring_dan_evaluasi_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_monitoring_dan_evaluasi',
            name='jenis',
            field=models.CharField(choices=[('monitoring_dan_evaluasi_kerja', 'Monitoring dan Evaluasi Kerja'), ('monitoring_dan_evaluasi_dalam_rangka_pendampingan', 'Monitoring dan Evaluasi dalam rangka pendampingan')], default='monitoring_dan_evaluasi_kerja', max_length=50),
        ),
        migrations.AddField(
            model_name='dayatif_monitoring_dan_evaluasi',
            name='periode',
            field=models.CharField(choices=[('triwulan', 'Triwulan'), ('semester', 'Semester'), ('tahunan', 'Tahunan')], default='triwulan', max_length=10),
        ),
        migrations.AddField(
            model_name='dayatif_monitoring_dan_evaluasi',
            name='satker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dayatif_monitoring_dan_evaluasi_satker', to='users.satker', verbose_name='SATUAN KERJA PELAKSANA'),
        ),
        migrations.AddField(
            model_name='dayatif_monitoring_dan_evaluasi',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dayatif_monitoring_dan_evaluasi',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_monitoring_dan_evaluasi_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_pemetaan_potensi_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='satker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dayatif_pemetaan_potensi_satker', to='users.satker', verbose_name='SATUAN KERJA PELAKSANA'),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_potensi',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_pemetaan_potensi_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_stakeholder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_stakeholder',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_pemetaan_stakeholder_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_stakeholder',
            name='satker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dayatif_pemetaan_stakeholder_satker', to='users.satker', verbose_name='SATUAN KERJA PELAKSANA'),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_stakeholder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dayatif_pemetaan_stakeholder',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_pemetaan_stakeholder_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_rapat_sinergi_stakeholder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayatif_rapat_sinergi_stakeholder',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_rapat_sinergi_stakeholder_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dayatif_rapat_sinergi_stakeholder',
            name='satker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dayatif_rapat_sinergi_stakeholder_satker', to='users.satker', verbose_name='SATUAN KERJA PELAKSANA'),
        ),
        migrations.AddField(
            model_name='dayatif_rapat_sinergi_stakeholder',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='dayatif_rapat_sinergi_stakeholder',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dayatif_rapat_sinergi_stakeholder_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='dayatif_bimbingan_teknis_lifeskill',
            table='kegiatan_dayatif_bimbingan_teknis_lifeskill',
        ),
        migrations.AlterModelTable(
            name='dayatif_bimbingan_teknis_stakeholder',
            table='kegiatan_dayatif_bimbingan_teknis_stakeholder',
        ),
        migrations.AlterModelTable(
            name='dayatif_dukungan_stakeholder',
            table='kegiatan_dayatif_dukungan_stakeholder',
        ),
        migrations.AlterModelTable(
            name='dayatif_monitoring_dan_evaluasi',
            table='kegiatan_dayatif_monitoring_dan_evaluasi',
        ),
        migrations.AlterModelTable(
            name='dayatif_pemetaan_potensi',
            table='kegiatan_dayatif_pemetaan_potensi',
        ),
        migrations.AlterModelTable(
            name='dayatif_pemetaan_stakeholder',
            table='kegiatan_dayatif_pemetaan_stakeholder',
        ),
        migrations.AlterModelTable(
            name='dayatif_rapat_sinergi_stakeholder',
            table='kegiatan_dayatif_rapat_sinergi_stakeholder',
        ),
    ]