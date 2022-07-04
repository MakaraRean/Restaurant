"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Restaurant.settings import MIDDLEWARE
from myrestaurant import views,viewsAdmin, viewsCategory, viewsFood

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',views.log_in,name="login"),
    path('logout/',views.log_out,name="logout"),

    #path('test/',views.test,name='test'),
    path('',views.home,name='home'),
    path('category/',views.category,name='category'),
    path('food/',views.food,name='food'),
    path('food/order/<id>',views.order,name='order'),
    path('food/orders/confirm-order/',views.orderList,name='orderList'),
    path('food/orders/show-order',views.showOrder,name="showOrder"),
    path('delete/<int:id>',views.deleteItem,name="deleteItem"),
    path('category/<id>',views.showByCategory,name="showByCategory"),
    path('confirm-order-by-category/<id>',views.confirmOrderByCategory),
    path('checkout',views.checkout,name="checkout"),
    path('empty-cart',views.emptyCart,name="emptyCart"),

    path('admin-dashboard/',views.dashboard,name='admin-dashboard'),

    # admin only
    path('home-admin/', viewsAdmin.is_admin, name='home-admin'),
    # CRUD users
    path('user/', views.user, name='user'),
    path('createUser/', views.createUser, name='createUser'),
    path('adduser',views.adduser, name='adduser'),
    path("user/editrow/<id>", views.editrow, name="editrow"),
    path("user/deleterow/<id>", views.deleterow, name="deleterow"), 
    path("user/update/<id>", views.update, name="update"),
    # CRUD Category
    path("category-admin/", viewsCategory.category, name="category-admin"),
    path("addcategory/",viewsCategory.addCategory,name="addcategory"),
    path("createCategory", viewsCategory.createCategory, name="createCategory"),
    path("deleteCat/<id>", viewsCategory.deleteCat, name="deleteCat"),
    path("editCat/<id>", viewsCategory.editCat, name="editCat"),
    path("updateCat/<id>", viewsCategory.updateCat, name="updateCat"),
    # Food
    path("food-admin/", viewsFood.food, name="food-admin"),
    path("createFood", viewsFood.createFood, name="createFood"),
    path("addfood", viewsFood.addFood, name="addfood"),
    path("deleteFood/<id>", viewsFood.deleteFood, name="deleteFood"),
    path("editFood/<id>", viewsFood.editFood, name="editFood"),
    path("updateFood/<id>", viewsFood.updateFood, name="updateFood"),
    # User
    path('user', views.user, name='user'),
    path('createUser', views.createUser, name='createUser'),
    path('adduser',views.adduser, name='adduser'),
    path("deleterow/<id>", views.deleterow, name="deleterow"),
    path("editrow/<id>", views.editrow, name="editrow"),
    path("update/<id>", views.update, name="update"),
]
MIDDLEWARE = [path('test/',views.test,name='test')]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)