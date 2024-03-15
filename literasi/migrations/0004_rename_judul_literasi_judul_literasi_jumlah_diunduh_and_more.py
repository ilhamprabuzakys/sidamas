# Generated by Django 4.1.7 on 2024-03-15 07:09

from django.db import migrations, models
import literasi.validators


class Migration(migrations.Migration):

    dependencies = [
        ('literasi', '0003_alter_literasi_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='literasi',
            old_name='Judul',
            new_name='judul',
        ),
        migrations.AddField(
            model_name='literasi',
            name='jumlah_diunduh',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='literasi',
            name='dokumen',
            field=models.FileField(null=True, upload_to='upload/files/literasi', validators=[literasi.validators.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='literasi',
            name='kategori',
            field=models.CharField(choices=[('buku', 'Buku'), ('video', 'Video'), ('audio', 'Audio'), ('video_youtube', 'Video Youtube')], default='1', max_length=15),
        ),
        migrations.AlterField(
            model_name='literasi',
            name='status',
            field=models.CharField(choices=[('published', 'PUBLISHED'), ('archived', 'ARCHIVED'), ('draft', 'DRAFT')], default='1', max_length=15),
        ),
    ]
