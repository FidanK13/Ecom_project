# Generated by Django 3.2.6 on 2021-10-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0020_banner_clientbrand_electronicsproduct_latest_blog_menproduct_redcard_sportsproduct_womenproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='sub_categories',
            field=models.BooleanField(default=False),
        ),
    ]