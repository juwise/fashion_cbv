# Generated by Django 2.1.1 on 2020-04-01 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anoapp', '0006_fashion_image1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fashion',
            name='image1',
        ),
    ]