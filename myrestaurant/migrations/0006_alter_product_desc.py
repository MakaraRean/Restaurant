# Generated by Django 3.2.13 on 2022-06-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrestaurant', '0005_remove_product_categorytype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
