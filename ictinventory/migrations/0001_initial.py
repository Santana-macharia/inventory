# Generated by Django 5.0.1 on 2024-01-05 06:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centre_id', models.CharField(editable=False, max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.CharField(editable=False, max_length=10, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ITStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(editable=False, max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('e_mail', models.EmailField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MohiUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(editable=False, max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('e_mail', models.EmailField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(editable=False, max_length=10, unique=True)),
                ('serial_number', models.CharField(max_length=50)),
                ('device_model', models.CharField(max_length=50)),
                ('device_condition', models.CharField(choices=[('option1', 'Good'), ('option2', 'Fair')], max_length=50)),
                ('status', models.CharField(choices=[('option1', 'Issued'), ('option2', 'Not Issued'), ('option3', 'Returned')], max_length=50)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ictinventory.centre')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ictinventory.department')),
                ('it_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ictinventory.itstaff')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ictinventory.mohiuser')),
            ],
        ),
    ]
