# Generated by Django 5.0.3 on 2024-05-17 19:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_student_identifier_student_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='skill',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
