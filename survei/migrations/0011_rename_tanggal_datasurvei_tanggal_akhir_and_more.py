# Generated by Django 4.1.7 on 2024-01-31 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survei', '0010_alter_datasurvei_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datasurvei',
            old_name='tanggal',
            new_name='tanggal_akhir',
        ),
        migrations.AddField(
            model_name='datasurvei',
            name='tanggal_awal',
            field=models.DateField(blank=True, null=True),
        ),
    ]
