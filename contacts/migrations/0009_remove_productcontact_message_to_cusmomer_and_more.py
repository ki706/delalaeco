# Generated by Django 4.1.3 on 2022-12-07 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_alter_productcontact_message_to_cusmomer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcontact',
            name='message_to_cusmomer',
        ),
        migrations.AddField(
            model_name='productcontact',
            name='message_to_customer',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='message to customer'),
        ),
    ]
