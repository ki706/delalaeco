# Generated by Django 4.1.3 on 2022-12-06 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_product_options_alter_service_options_and_more'),
        ('contacts', '0005_rename_car_id_servicecontact_ser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcontact',
            name='car_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.product', verbose_name='product id'),
        ),
    ]