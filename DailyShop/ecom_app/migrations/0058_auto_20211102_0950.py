# Generated by Django 3.2.7 on 2021-11-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0057_alter_latest_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_1',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_2',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_3',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_4',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image_5',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='catalog_products',
            name='image',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='clientbrand',
            name='image',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='redcard',
            name='image',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='background_image',
            field=models.ImageField(default='miles.jpg', upload_to='shop_images'),
        ),
    ]