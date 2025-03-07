# Generated by Django 5.0.12 on 2025-03-05 10:18

import backend.files.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=backend.files.utils.file_generate_upload_path)),
                ('original_file_name', models.TextField()),
                ('file_name', models.CharField(max_length=255, unique=True)),
                ('file_type', models.CharField(max_length=255)),
                ('upload_finished_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
