# Generated by Django 3.1.1 on 2024-01-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_auto_20240116_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importdevice',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='centre',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='date',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='hardware',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='hdd',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='physicalconfirmation',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='processor',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='serial_number',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='status',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='system_model',
        ),
        migrations.RemoveField(
            model_name='importdevice',
            name='uaf_signed',
        ),
        migrations.AddField(
            model_name='importdevice',
            name='csv_file',
            field=models.FileField(null=True, upload_to='uploaded_csv_files/'),
        ),
    ]
