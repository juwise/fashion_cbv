# Generated by Django 2.1.1 on 2020-04-06 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anoapp', '0013_image_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='post',
        ),
        migrations.AddField(
            model_name='fashion',
            name='image',
            field=models.ImageField(default='image_pics/default.jpg', upload_to='image_pics/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
