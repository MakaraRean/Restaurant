import email
from operator import mod
from pydoc import describe
from re import A
from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255,null=True)
    desc = models.TextField(null=True)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField(null=True,blank=True)
    image_path = models.CharField(max_length=255,null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class Table(models.Model):
    tableNumber = models.IntegerField()
    desc = models.TextField(null=True)
    active = models.BooleanField(default=False)

class User(models.Model):
    full_name = models.CharField(max_length=25)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)

class Order(models.Model):
    order_date = models.DateTimeField()
    total = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    table = models.ForeignKey(Table,on_delete=models.CASCADE)

class OrderDetail(models.Model):
    amount = models.FloatField()
    qty = models.IntegerField()
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)