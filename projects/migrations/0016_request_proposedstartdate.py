# Generated by Django 4.0.8 on 2022-12-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='proposedStartDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
