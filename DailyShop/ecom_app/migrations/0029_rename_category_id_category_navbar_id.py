# Generated by Django 3.2.7 on 2021-10-12 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0028_auto_20211010_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_id',
            new_name='navbar_id',
        ),
    ]
