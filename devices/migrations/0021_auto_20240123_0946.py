# Generated by Django 3.2.23 on 2024-01-23 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0020_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='import',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
