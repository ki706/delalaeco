# Generated by Django 4.1.3 on 2022-12-04 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_contact_productcontact_servicecontact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicecontact',
            old_name='ser_id',
            new_name='car_id',
        ),
    ]
