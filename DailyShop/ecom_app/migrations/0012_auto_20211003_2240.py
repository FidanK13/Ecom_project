# Generated by Django 3.2.7 on 2021-10-03 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0011_auto_20211003_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images')),
            ],
        ),
        migrations.RenameModel(
            old_name='ProductModel',
            new_name='ProductModel_1',
        ),
    ]