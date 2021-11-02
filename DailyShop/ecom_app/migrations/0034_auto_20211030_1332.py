# Generated by Django 3.2.7 on 2021-10-30 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0033_menproduct_name_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop_images')),
                ('related_navbar', models.ManyToManyField(to='ecom_app.NavbarModel')),
            ],
        ),
        migrations.DeleteModel(
            name='ElectronicsProduct',
        ),
        migrations.DeleteModel(
            name='MenProduct',
        ),
        migrations.DeleteModel(
            name='SportsProduct',
        ),
        migrations.DeleteModel(
            name='WomenProduct',
        ),
    ]
