# Generated by Django 3.2.13 on 2022-06-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrestaurant', '0009_alter_category_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image_path',
            field=models.ImageField(upload_to='myrestaurant/static/images/'),
        ),
    ]