# Generated by Django 3.1.7 on 2021-05-22 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_auto_20210522_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='received_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='payment_details',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
