# Generated by Django 3.2.7 on 2021-10-05 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0020_clientbrand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='brand_images',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='latest_blog_images',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='latest_blog_text',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='redcard_image',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='redcard_name',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='redcard_text',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='redcard_url',
        ),
    ]
