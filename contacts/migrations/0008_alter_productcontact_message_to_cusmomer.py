# Generated by Django 4.1.3 on 2022-12-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_productcontact_message_to_cusmomer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcontact',
            name='message_to_cusmomer',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='message to cusmomer'),
        ),
    ]