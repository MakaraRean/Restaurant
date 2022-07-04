from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from myrestaurant.models import  Category, Victual


def food(request):
    if request.user.isAdmin:
        food = Victual.objects.all()
        context = {'foods': food}
        return render(request, 'Food/food.html', context)
    else:
        return render(request,'404.html')
def addFood(request):
    if request.user.isAdmin:
        try:
            # if request.method == 'POST':
            foods = Victual()
            foods.name = request.POST['name']
            foods.price = request.POST['price']
            foods.desc = request.POST['desc']
            foods.active = 'f'
            foods.created_at = datetime.now()
            foods.category_id = request.POST['category_id']
            if len(request.FILES)>0:
                foods.image_path = request.FILES['image_path']
                foods.save()
                messages.success(request, 'Victual Add Success')
            else:
                foods.image_path = 'no_image.jpg'
                foods.save()
                messages.success(request, 'Victual Add Success')
        except Exception as ex:
            print(ex)
        return redirect(food)
    else:
        return render(request,'404.html')
def createFood(request):
    if request.user.isAdmin:
        categories = Category.objects.all()
        context = {'cats': categories}
        return render(request, 'Food/addFood.html', context)
    else:
        return render(request,'404.html')
def deleteFood(request, id):
    if request.user.isAdmin:
        try:
            foods = Victual.objects.get(pk=id)
            foods.delete()
            pass
        except Exception as ex:
            print(ex)
        return redirect(food)
    else:
        return render(request,'404.html')
def editFood(request, id):
    if request.user.isAdmin:
        try:
            foods = Victual.objects.get(pk=id)
            categories = Category.objects.all()
            context={
                'food': foods,
                'category': categories
            }
        except Exception as ex:
            print(ex)
        return render(request, 'Food/editFood.html', context)
    else:
        return render(request,'404.html')
def updateFood(request, id):
    if request.user.isAdmin:
        try:
                foods = Victual()
                foods.id = id
                foods.name = request.POST['name']
                foods.price = request.POST['price']
                foods.desc = request.POST['desc']
                foods.image_path = request.FILES['image_path']
                foods.active = 'f'
                foods.created_at = ''
                foods.category_id = request.POST['category_id']
                foods.save()
                messages.success(request, 'Update Successfully')

        except Exception as ex:
            print(ex)
        return redirect(food)
    else:
        return render(request,'404.html')






