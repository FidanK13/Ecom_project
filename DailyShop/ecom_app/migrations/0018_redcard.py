# Generated by Django 3.2.7 on 2021-10-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0017_electronicsproduct_sportsproduct_womenproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images')),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
