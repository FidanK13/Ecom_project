# Generated by Django 3.2.7 on 2021-10-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0036_alter_latest_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latest_blog',
            name='image',
            field=models.ImageField(blank=True, default='~/Downloads/148713801_1534855573379535_8524425501051131545_n.jpg', null=True, upload_to='shop_images'),
        ),
    ]
