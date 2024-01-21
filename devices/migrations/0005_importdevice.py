# Generated by Django 5.0.1 on 2024-01-16 08:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_alter_alldevice_id'),
        ('ictinventory', '0008_alter_centre_id_alter_department_id_alter_device_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Importdevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware', models.CharField(max_length=200)),
                ('system_model', models.CharField(max_length=200)),
                ('processor', models.CharField(max_length=200)),
                ('ram', models.CharField(max_length=100)),
                ('hdd', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Good', 'Good'), ('Fair', 'Fair')], max_length=100)),
                ('physicalconfirmation', models.CharField(choices=[('Correct', 'Correct'), ('Incorrect', 'Incorrect')], max_length=100)),
                ('uaf_signed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('comments', models.CharField(max_length=500)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ictinventory.mohiuser')),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ictinventory.centre')),
            ],
        ),
    ]
