# Generated by Django 4.1.7 on 2024-01-29 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survei', '0008_datasurvei_dikirimkan_kepada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasurvei',
            old_name='jumlah_responden',
            new_name='batas_responden',
        ),
    ]
