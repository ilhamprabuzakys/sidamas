# Generated by Django 3.2.24 on 2024-02-27 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survei', '0013_auto_20240221_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasurvei',
            name='keterangan',
            field=models.TextField(blank=True, null=True),
        ),
    ]
