# Generated by Django 3.1.7 on 2021-05-29 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0008_auto_20210529_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
