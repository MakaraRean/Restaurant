from logging import error
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,  redirect
from myrestaurant.carts import Cart
from django.contrib.auth import authenticate, login, logout
from myrestaurant.models import Category, Order, OrderDetail, OrderItem, Victual
from django.contrib import messages
from django.db.models import Sum, Count

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
    if request.user.is_authenticated:
        victual = Victual.objects.all()
        category = Category.objects.all()
        cartItem = OrderItem.objects.aggregate(Count('id'))
        context = {'victuals': victual,'categories' : category, 'cartItem' : cartItem}
        return render(request,'home.html',context)
    else:
        return render(request,'test.html')

def order(request, id ):
    victuals = Victual.objects.get(id = id)
    return render(request,'order.html',{'victual' : victuals})

def category(request):
    category = Category.objects.all()
    cartItem = OrderItem.objects.aggregate(Count('id'))
    return render(request,'category.html',{'categories' : category, 'cartItem' : cartItem})

def dashboard(request):
    return render(request,'admin/index.html')

def food(request):
    victuals = Victual.objects.all()
    cartItem = OrderItem.objects.aggregate(Count('id'))
    return render(request,'food.html',{'victuals' : victuals, 'cartItem' : cartItem})

def orderList(request):
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
                orderItem.save()

        messages.success(request, "Items added to Cart.")
        return redirect(home)

def showOrder(request):
    orderItems = OrderItem.objects.all()
    total = OrderItem.objects.aggregate(Sum('amount'))
    cartItem = OrderItem.objects.aggregate(Count('id'))
    return render(request,'showOrder.html',{'orderItems' : orderItems,'total' : total, 'cartItem' : cartItem})
            
def deleteItem(request, id):
    item = OrderItem.objects.get(pk = id)
    item.delete()
    messages.success(request, "An item has been remove from cart.")
    return HttpResponseRedirect(reverse('showOrder'))

def showByCategory(request, id):
    cartItem = OrderItem.objects.aggregate(Count('id'))
    cat = Category.objects.get(pk = id)
    victual = Victual.objects.filter(category_id = id)
    return render(request,'show-by-category.html',{'victuals' : victual, 'cat' : cat, 'cartItem' : cartItem})

def confirmOrderByCategory(request, id):
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
                orderItem.save()

        messages.success(request, "Items added to Cart.")
        return redirect(home)

def checkout(request):
    if request.method == 'POST':
        order = Order()
        orderDetial = OrderDetail()
        total = 0.0
    return True