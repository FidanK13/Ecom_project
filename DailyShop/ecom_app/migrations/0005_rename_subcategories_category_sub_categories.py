# Generated by Django 3.2.7 on 2021-10-03 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0004_auto_20211003_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='subcategories',
            new_name='sub_categories',
        ),
    ]
