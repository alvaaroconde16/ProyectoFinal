# Generated by Django 5.1.7 on 2025-04-01 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='peluqueria',
        ),
    ]
