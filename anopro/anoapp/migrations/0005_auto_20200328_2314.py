# Generated by Django 2.1.1 on 2020-03-28 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anoapp', '0004_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='comment',
            field=models.TextField(),
        ),
    ]
