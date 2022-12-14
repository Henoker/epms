# Generated by Django 4.0.8 on 2022-12-27 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_quotation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('RequestDate', models.DateField(blank=True, null=True)),
                ('clientDeadline', models.DateField(blank=True, null=True)),
                ('source_languages', models.CharField(blank=True, max_length=300, null=True)),
                ('target_languages', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(choices=[('ETB', 'BIRR'), ('$', 'USD')], default='ETB', max_length=100)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.client')),
                ('quote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.quotation')),
            ],
        ),
    ]
