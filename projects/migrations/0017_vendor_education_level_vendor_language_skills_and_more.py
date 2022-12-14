# Generated by Django 4.0.8 on 2023-01-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_request_proposedstartdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='education_level',
            field=models.CharField(blank=True, choices=[('CERTIFICATE', 'CERTIFICATE'), ('DIPLOMA', 'DIPLOMA'), ('UNIVERSITY DEGREE', 'UNIVERSITY DEGREE'), ('GRADUATE DEGREE', 'GRADUATE DEGREE'), ('DOCTORIAL LEVEL', 'DOCTORIAL LEVEL')], max_length=100),
        ),
        migrations.AddField(
            model_name='vendor',
            name='language_skills',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='lingustic_level',
            field=models.CharField(blank=True, choices=[('NOVICE', 'NOVICE'), ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')], max_length=100),
        ),
    ]
