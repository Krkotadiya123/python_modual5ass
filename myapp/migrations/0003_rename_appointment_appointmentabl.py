# Generated by Django 4.2 on 2024-12-23 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_doctor_tbl_email_alter_patient_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='appointment',
            new_name='appointmentabl',
        ),
    ]
