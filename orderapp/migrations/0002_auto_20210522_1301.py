# Generated by Django 3.1.7 on 2021-05-22 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_products_stock'),
        ('orderapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_item',
            name='product_id',
        ),
        migrations.AddField(
            model_name='order_item',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.products'),
            preserve_default=False,
        ),
    ]
