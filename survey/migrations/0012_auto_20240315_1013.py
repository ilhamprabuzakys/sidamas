# Generated by Django 3.2.24 on 2024-03-15 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_auto_20240315_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='user',
        ),
        migrations.AddField(
            model_name='survey',
            name='pemilik',
            field=models.CharField(choices=[('1', 'PSM'), ('2', 'DAYATIF')], default='1', max_length=1),
        ),
    ]