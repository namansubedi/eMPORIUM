# Generated by Django 3.2.3 on 2021-05-17 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_products_category'),
        ('cart', '0002_auto_20210517_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.products'),
        ),
    ]
