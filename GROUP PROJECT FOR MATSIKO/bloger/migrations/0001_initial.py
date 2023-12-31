# Generated by Django 4.2.6 on 2023-11-05 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpName', models.CharField(max_length=20)),
                ('EmpSex', models.CharField(max_length=20)),
                ('EmpTitle', models.CharField(max_length=10)),
                ('EmpDob', models.DateField()),
                ('EmpStatus', models.CharField(max_length=10)),
                ('EmpAddress', models.CharField(max_length=10, null=True)),
                ('EmpContact', models.CharField(max_length=10)),
                ('EmpEmail', models.EmailField(max_length=254)),
                ('EmpQualfication', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Employees',
            },
        ),
    ]
