# Generated by Django 3.1.7 on 2021-05-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0009_remove_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_details',
            name='seller_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
