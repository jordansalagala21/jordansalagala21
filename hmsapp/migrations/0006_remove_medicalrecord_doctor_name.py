# Generated by Django 4.2.7 on 2023-11-27 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hmsapp', '0005_doctor_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='doctor_name',
        ),
    ]