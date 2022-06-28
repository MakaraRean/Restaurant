from django.contrib import admin

from .models import Category, Table, User, Victual

admin.site.register(Category)
admin.site.register(Victual)
admin.site.register(Table)
admin.site.register(User)

# Register your models here.
