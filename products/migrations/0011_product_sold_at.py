# Generated by Django 2.1.5 on 2020-04-24 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200424_0142'),
        ('products', '0010_product_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sold_at',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Event'),
        ),
    ]