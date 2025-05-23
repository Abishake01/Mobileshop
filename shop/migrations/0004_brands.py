# Generated by Django 5.0.7 on 2024-09-29 13:25

import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_trending'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=150)),
                ('brand_logo', models.ImageField(blank=True, null=True, upload_to=shop.models.getFileName)),
            ],
        ),
    ]
