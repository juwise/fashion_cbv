# Generated by Django 2.1.1 on 2020-03-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anoapp', '0005_auto_20200328_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='fashion',
            name='image1',
            field=models.ImageField(default='image_pics/default.jpg', upload_to='image_pics/'),
        ),
    ]