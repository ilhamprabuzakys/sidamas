# Generated by Django 3.2.24 on 2024-03-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survei', '0015_auto_20240301_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datarespondensurvei',
            name='handphone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
