# Generated by Django 3.2.7 on 2021-10-31 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0041_auto_20211031_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog_products',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='shop_images'),
        ),
        migrations.AddField(
            model_name='catalog_products',
            name='size_L',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='catalog_products',
            name='size_M',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='catalog_products',
            name='size_S',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='catalog_products',
            name='size_XL',
            field=models.BooleanField(default=True),
        ),
    ]