# Generated by Django 4.1.7 on 2023-11-07 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodule', '0003_alter_user_hasil_alter_user_nilai'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]