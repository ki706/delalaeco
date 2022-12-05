# Generated by Django 4.1.3 on 2022-12-04 08:54

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('skill', models.CharField(max_length=1000)),
                ('experiance', models.PositiveSmallIntegerField()),
                ('location', models.CharField(choices=[('Addis Ababa', 'Addis Ababa'), ('Gondar', 'Gondar'), ('Dessie', 'Dessie'), ('Bahirdar', 'Bahirdar'), ('Semera', 'Semera')], max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('is_avilable', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('service_pics', models.ImageField(upload_to='pro_pics/%Y/%m/%d/')),
                ('service_pics1', models.FileField(upload_to='pro_pics/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.servicecatagory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(choices=[('Addis Ababa', 'Addis Ababa'), ('Gondar', 'Gondar'), ('Dessie', 'Dessie'), ('Bahirdar', 'Bahirdar'), ('Semera', 'Semera')], max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('is_avilable', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('product_pics', models.ImageField(upload_to='pro_pics/%Y/%m/%d/')),
                ('product_pics1', models.FileField(upload_to='pro_pics/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.productcatagory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
