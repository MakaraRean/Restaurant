# Generated by Django 3.2.13 on 2022-06-18 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_path', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('image_path', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableNumber', models.IntegerField()),
                ('desc', models.TextField()),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('isAdmin', models.BooleanField(default=False)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('desc', models.TextField()),
                ('image_path', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('categoryType_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.categorytype')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('qty', models.IntegerField()),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.category')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.user'),
        ),
        migrations.AddField(
            model_name='category',
            name='categoryType_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myrestaurant.categorytype'),
        ),
    ]
