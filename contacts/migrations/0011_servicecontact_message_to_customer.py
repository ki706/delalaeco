# Generated by Django 4.1.3 on 2022-12-08 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_alter_productcontact_message_to_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecontact',
            name='message_to_customer',
            field=models.TextField(blank=True, null=True, verbose_name='message to customer'),
        ),
    ]