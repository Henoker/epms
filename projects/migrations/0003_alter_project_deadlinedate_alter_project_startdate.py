# Generated by Django 4.0.8 on 2022-11-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_budgetedamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadlineDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
