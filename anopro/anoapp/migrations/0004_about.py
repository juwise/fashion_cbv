# Generated by Django 2.1.1 on 2020-03-28 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anoapp', '0003_auto_20200324_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
    ]
