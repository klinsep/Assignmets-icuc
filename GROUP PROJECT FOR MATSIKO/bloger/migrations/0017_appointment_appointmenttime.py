# Generated by Django 4.2.6 on 2023-11-07 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloger', '0016_alter_customer_address_alter_customer_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='AppointmentTime',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]