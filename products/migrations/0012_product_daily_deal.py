# Generated by Django 2.1.5 on 2020-04-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_sold_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='daily_deal',
            field=models.BooleanField(default=False),
        ),
    ]
