# Generated by Django 3.2.13 on 2022-06-28 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myrestaurant', '0023_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
