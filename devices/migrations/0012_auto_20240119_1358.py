# Generated by Django 3.1.1 on 2024-01-19 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0011_auto_20240119_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='import',
            name='assigned_by',
        ),
        migrations.RemoveField(
            model_name='import',
            name='assignee_email_address',
        ),
        migrations.RemoveField(
            model_name='import',
            name='assignee_first_name',
        ),
        migrations.RemoveField(
            model_name='import',
            name='assignee_last_name',
        ),
        migrations.RemoveField(
            model_name='import',
            name='centre',
        ),
        migrations.RemoveField(
            model_name='import',
            name='department',
        ),
        migrations.RemoveField(
            model_name='import',
            name='device_condition',
        ),
        migrations.RemoveField(
            model_name='import',
            name='device_name',
        ),
        migrations.RemoveField(
            model_name='import',
            name='hardware',
        ),
        migrations.RemoveField(
            model_name='import',
            name='hdd_gb',
        ),
        migrations.RemoveField(
            model_name='import',
            name='processor',
        ),
        migrations.RemoveField(
            model_name='import',
            name='ram_gb',
        ),
        migrations.RemoveField(
            model_name='import',
            name='serial_number',
        ),
        migrations.RemoveField(
            model_name='import',
            name='status',
        ),
        migrations.RemoveField(
            model_name='import',
            name='system_model',
        ),
    ]
