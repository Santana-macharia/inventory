# Generated by Django 3.1.1 on 2024-01-19 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ictinventory', '0010_auto_20240119_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='device_model',
            new_name='system_model',
        ),
        migrations.RenameField(
            model_name='mohiuser',
            old_name='e_mail',
            new_name='assignee_email_address',
        ),
        migrations.RenameField(
            model_name='mohiuser',
            old_name='first_name',
            new_name='assignee_first_name',
        ),
        migrations.RenameField(
            model_name='mohiuser',
            old_name='last_name',
            new_name='assignee_last_name',
        ),
    ]
