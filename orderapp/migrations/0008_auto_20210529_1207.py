# Generated by Django 3.1.7 on 2021-05-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0007_auto_20210524_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Delivering', 'Delivering'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], max_length=20),
        ),
        migrations.AlterField(
            model_name='order_item',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Delivering', 'Delivering'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], max_length=10),
        ),
        migrations.AlterField(
            model_name='payment_details',
            name='provider',
            field=models.CharField(choices=[('eSewa', 'eSewa'), ('Cash On Delivery', 'Cash On Delivery')], max_length=20),
        ),
        migrations.AlterField(
            model_name='payment_details',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], max_length=10),
        ),
    ]
