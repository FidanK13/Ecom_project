# Generated by Django 3.2.7 on 2021-10-31 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0046_auto_20211031_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog_products',
            name='color',
        ),
        migrations.DeleteModel(
            name='colors',
        ),
    ]