# Generated by Django 3.1.7 on 2021-07-12 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210702_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
    ]