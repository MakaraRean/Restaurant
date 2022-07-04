from datetime import datetime
import imp
from logging import error
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,  redirect
from myrestaurant.carts import Cart
from django.contrib.auth import authenticate, login, logout
from myrestaurant.models import Category, Order, OrderDetail, OrderItem, Table, User, Victual
from django.contrib import messages
from django.db.models import Sum, Count
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

def log_in(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.isAdmin: 
                return redirect(home)
            else:
                # Redirect to a success page.
                return redirect(home)
            ...
        else:
            # Return an 'invalid login' error message.
            messages.success(request,"Wrong username or password")
            return redirect(log_in)
            ...

def log_out(request):
    logout(request)
    return redirect(log_in)

def test(request):
    return render(request,'test.html')

def home(request):
    if request.user.is_authenticated and request.user.isAdmin == False:
        victual = Victual.objects.all()
        category = Category.objects.all()
        cartItem = OrderItem.objects.aggregate(Count('id'))
        context = {'victuals': victual,'categories' : category, 'cartItem' : cartItem}
        return render(request,'home.html',context)
    elif request.user.is_anonymous:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

    elif request.user.isAdmin:
        return render(request,'home-admin.html')
    
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

def order(request, id ):
    if request.user.is_authenticated and request.user.isAdmin == False:
        victuals = Victual.objects.get(id = id)
        return render(request,'order.html',{'victual' : victuals})
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

# CRUD users
def user(request):
    if request.user.isAdmin:
        user = User.objects.all()
        context = {'users': user}
        return render(request, "User/users.html", context)
    else:
        return render(request,'404.html')

def createUser(request):
    if request.user.isAdmin:
        return render(request, "User/addUser.html")
    else:
        return render(request,'404.html')

def adduser(request):
    if request.user.isAdmin:
        try:
            add = User()
            add.full_name = request.POST['full_name']
            add.username = request.POST['username']
            add.password = make_password(request.POST['password'])
            add.save()
            messages.success(request, 'Save Success')
        except Exception as ex:
            print(ex)
        return redirect(user)
    else:
        return render(request,'404.html')

def deleterow(request, id):
    if request.user.isAdmin:
        try:
            tbluser = User.objects.get(pk=id)
            tbluser.delete()
            pass
        except Exception as ex:
            print(ex)
        return redirect('user')
    else:
        return render(request,'404.html')
def editrow(request, id):
    if request.user.isAdmin:
        try:
            tbluser = User.objects.get(pk=id)
            context ={
                "users": tbluser
            }
        except Exception as ex:
            print(ex)
        return render(request, "User/editUser.html", context)
    else:
        return render(request,'404.html')
def update(request, id):
    if request.user.isAdmin:
        try:
            users = User()
            users.id = id
            users.full_name = request.POST['full_name']
            users.username = request.POST['username']
            users.password = make_password(request.POST['password'])
            users.save()
            messages.success(request, 'User update successfully')
        except Exception as ex:
            print(ex)
        return redirect(user)
    else:
        return render(request,'404.html')
# end CRUD users

    
def category(request):
    if request.user.is_authenticated and request.user.isAdmin == False:
        category = Category.objects.all()
        cartItem = OrderItem.objects.aggregate(Count('id'))
        return render(request,'category.html',{'categories' : category, 'cartItem' : cartItem})
    elif request.user.isAdmin:
        categories = Category.objects.all()
        context = {'cats': categories}
        return render(request, 'Category/category.html', context)
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

def dashboard(request):
    return render(request,'index.html')

def food(request):
    if request.user.is_authenticated and request.user.isAdmin == False:
        victuals = Victual.objects.all()
        cartItem = OrderItem.objects.aggregate(Count('id'))
        return render(request,'food.html',{'victuals' : victuals, 'cartItem' : cartItem})
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

def orderList(request):
    if request.user.is_authenticated and request.user.isAdmin == False:
        if request.method == 'POST':
            victuals = Victual.objects.all()
            for victual in victuals:
                name = "qty-"
                qty = name + str(victual.id)
                valueQty = request.POST[qty]
                cart = Cart()
                # Add to list or database
                if int(valueQty) > 0:
                    orderItem = OrderItem()
                    orderItem.name = victual.name
                    orderItem.qty = valueQty
                    orderItem.price = victual.price
                    orderItem.amount = (float(orderItem.qty) * orderItem.price)
                    orderItem.image_path = victual.image_path
                    orderItem.victual_id = victual.id
                    orderItem.user_id = request.user.id
                    orderItem.save()

            messages.success(request, "Items added to Cart.")
            return redirect(home)
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

def showOrder(request):
    if request.user.is_authenticated and request.user.isAdmin == False:
        orderItems = OrderItem.objects.filter(user_id = request.user.id)
        total = OrderItem.objects.aggregate(Sum('amount'))
        cartItem = OrderItem.objects.aggregate(Count('id'))
        tbls = Table.objects.filter(active = False)
        return render(request,'showOrder.html',{'orderItems' : orderItems,'total' : total, 'cartItem' : cartItem, 'tbls' : tbls})
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)
            
def deleteItem(request, id):
    if request.user.is_authenticated and request.user.isAdmin == False:
        item = OrderItem.objects.get(pk = id)
        item.delete()
        messages.success(request, "An item has been remove from cart.")
        return HttpResponseRedirect(reverse('showOrder'))
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

def showByCategory(request, id):
    if request.user.is_authenticated and request.user.isAdmin == False:
        cartItem = OrderItem.objects.aggregate(Count('id'))
        cat = Category.objects.get(pk = id)
        victual = Victual.objects.filter(category_id = id)
        return render(request,'show-by-category.html',{'victuals' : victual, 'cat' : cat, 'cartItem' : cartItem})
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

def confirmOrderByCategory(request, id):
    if request.user.is_authenticated and request.user.isAdmin == False:
        if request.method == 'POST':
            victuals = Victual.objects.filter(category_id = id)
            for victual in victuals:
                name = "qty-"
                qty = name + str(victual.id)
                valueQty = request.POST[qty]
                cart = Cart()
                # Add to list or database
                if int(valueQty) > 0:
                    orderItem = OrderItem()
                    orderItem.name = victual.name
                    orderItem.qty = valueQty
                    orderItem.price = victual.price
                    orderItem.amount = (float(orderItem.qty) * orderItem.price)
                    orderItem.image_path = victual.image_path
                    orderItem.victual_id = victual.id
                    orderItem.user_id = request.user.id
                    orderItem.save()

            messages.success(request, "Items added to Cart.")
            return redirect(home)
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

def checkout(request):
    if request.user.is_authenticated and request.user.isAdmin == False:
        if request.method == 'POST':
            order = Order()
            total = request.POST['total']
            orderDate = datetime.now()
            userID = request.user.id
            tableID = request.POST['tableID']
            # add to order
            order.order_date = orderDate
            order.total = total
            order.user_id = userID
            order.table_id = tableID
            order.save()
            # scope order id
            scope_order_id = (Order.objects.last()).id
            # add to orderdetail
            items = OrderItem.objects.all()
            for item in items:
                orderDetial = OrderDetail()
                price = request.POST['price-' + str(item.id)]
                qty = request.POST['qty-' + str(item.id)]
                orderID = scope_order_id
                victualID = item.victual_id

                orderDetial.price = price
                orderDetial.qty = qty
                orderDetial.order_id = orderID
                orderDetial.victual_id = victualID
                orderDetial.save()
            # update table ative to true   
            Table.objects.filter(pk=request.POST['tableID']).update(active = True)
            # delete item from cart
            item = OrderItem.objects.all()
            item.delete()
            messages.success(request,"Order successfully.")
            return redirect(home)
    else:
        messages.error(request, "You're not login, you need to login first.") 
        logout(request)
        return redirect(log_in)

def emptyCart(request):
    if request.user.is_authenticated and request.user.isAdmin == False:
        OrderItem.objects.all().delete()
        return redirect(showOrder)
    else:
        return not_login(request)

def not_login(request):
    messages.error(request, "You're not login, you need to login first.") 
    logout(request)
    return redirect(log_in)