import email
from operator import mod
from pydoc import describe
from re import A
from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.

class CategoryType(models.Model):
    type = models.CharField(max_length=50)
    image_path = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255)
    desc = models.TextField()
    categoryType_id = models.ForeignKey(CategoryType,on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField()
    image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    categoryType_id = models.ForeignKey(CategoryType,on_delete=models.CASCADE)

class Table(models.Model):
    tableNumber = models.IntegerField()
    desc = models.TextField()
    active = models.BooleanField(default=False)


class Staff(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    title = models.CharField(max_length=30)

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)

class Order(models.Model):
    order_date = models.DateTimeField()
    total = models.FloatField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

class OrderDetail(models.Model):
    amount = models.FloatField()
    qty = models.IntegerField()
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)