# Generated by Django 4.2 on 2024-12-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_tbl',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
