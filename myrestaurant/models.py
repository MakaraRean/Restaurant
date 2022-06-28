from distutils.command import upload
import email
from operator import mod
import os
from pydoc import describe
from re import A
from tkinter import CASCADE
from unicodedata import name
from urllib import request
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    #image_path = models.CharField(max_length=255,null=True)
    image_path = models.FileField(null=True, verbose_name="")
    desc = models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.name}"

class Victual(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.TextField(null=True,blank=True)
    image_path = models.FileField()
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name},   {self.price},  {self.category},    {self.active}"

class Table(models.Model):
    tableNumber = models.IntegerField()
    desc = models.TextField(null=True,blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tableNumber}"

class UserManager(BaseUserManager):
    # def create_user(self, username, full_name, password = None):
    #     user = self.model(username = username, full_name = full_name)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user

    # def create_superuser(self, username, full_name, password = None):
    #     user = self.create_user(username, full_name = full_name, password =  password)
    #     user.isAdmin = True
    #     user.is_superuser = True
    #     user.is_staff = True
    #     user.save(using=self._db)
    #     return user

    def create_user(self, username, full_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        # if not email:
        #     raise ValueError('Users must have an email address')

        user = self.model(
            username= username,
            full_name=full_name,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, full_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            password=password,
            full_name=full_name,
        )
        user.isAdmin = True
        user.save()
        return user

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=25)
    username = models.CharField(verbose_name='username', max_length=30,unique=True)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']
    

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.isAdmin

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
    product = models.ForeignKey(Victual,on_delete=models.CASCADE)

class OrderItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()
    amount = models.FloatField()
    image_path = models.FileField()
    victual = models.ForeignKey(Victual,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)