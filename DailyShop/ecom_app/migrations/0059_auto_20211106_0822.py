# Generated by Django 3.2.7 on 2021-11-06 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0058_auto_20211102_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_1',
            field=models.ImageField(default='promo-banner-1.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_2',
            field=models.ImageField(default='promo-banner-3.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_3',
            field=models.ImageField(default='promo-banner-3.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_4',
            field=models.ImageField(default='promo-banner-3.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_5',
            field=models.ImageField(default='promo-banner-3.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='catalog_products',
            name='background_image',
            field=models.ImageField(blank=True, default='fashion-header-bg-8.jpg', null=True, upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='catalog_products',
            name='image',
            field=models.ImageField(default='polo-shirt-1.png', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='clientbrand',
            name='image',
            field=models.ImageField(default='client-brand-css3.png', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='latest_blog',
            name='image',
            field=models.ImageField(default='promo-banner-1.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='redcard',
            name='image',
            field=models.ImageField(default='testimonial-img-1.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='background_image',
            field=models.ImageField(default='1.jpg', upload_to='shop_images'),
        ),
        migrations.DeleteModel(
            name='ProductModel',
        ),
    ]
