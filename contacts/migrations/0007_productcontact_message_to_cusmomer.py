# Generated by Django 4.1.3 on 2022-12-07 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_alter_productcontact_car_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcontact',
            name='message_to_cusmomer',
            field=models.CharField(max_length=100, null=True, verbose_name='message to cusmomer'),
        ),
    ]
