# Generated by Django 5.1.3 on 2024-11-22 02:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filefield', models.FileField(null=True, upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(['zip'])], verbose_name='attached file')),
            ],
        ),
    ]