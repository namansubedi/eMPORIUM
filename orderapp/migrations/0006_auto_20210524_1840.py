# Generated by Django 3.1.7 on 2021-05-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0005_order_item_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='received_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='received_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]