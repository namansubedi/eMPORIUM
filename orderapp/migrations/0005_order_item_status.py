# Generated by Django 3.1.7 on 2021-05-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0004_auto_20210524_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_item',
            name='status',
            field=models.CharField(choices=[('pro', 'Processing'), ('del', 'Delivering')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
