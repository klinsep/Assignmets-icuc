# Generated by Django 4.2.6 on 2023-11-05 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0008_remove_employee_id_employee_empid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='EmpQualfication',
            new_name='EmpQualification',
        ),
    ]
