# Generated by Django 4.0.8 on 2023-06-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_vendor_education_level_vendor_language_skills_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
