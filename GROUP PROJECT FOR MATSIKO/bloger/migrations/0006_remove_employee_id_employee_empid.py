# Generated by Django 4.2.6 on 2023-11-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0005_remove_employee_empid_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='EmpID',
            field=models.AutoField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
