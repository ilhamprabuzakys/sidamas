# Generated by Django 4.1.7 on 2024-01-18 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_survey_survey_result_surveyshort_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey_result',
            name='hasil',
            field=models.JSONField(blank=True, null=True),
        ),
    ]