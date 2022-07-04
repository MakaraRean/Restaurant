from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from myrestaurant.models import User, Category


def category(request):
    if request.user.isAdmin:
        categories = Category.objects.all()
        context = {'cats': categories}
        return render(request, 'Category/category.html', context)
    else:
        return render(request,'404.html')
def addCategory(request):
    if request.user.isAdmin:
        try:
            categories = Category()
            categories.name = request.POST['name']
            categories.image_path = request.FILES['image_path']
            categories.desc = request.POST['desc']
            categories.save()
        except Exception as ex:
            print(ex)
        return redirect(category)
    else:
        return render(request,'404.html')
def createCategory(request):
    if request.user.isAdmin:
        return render(request, 'Category/addCategory.html')
    else:
        return render(request,'404.html')
def deleteCat(request, id):
    if request.user.isAdmin:
        try:
            catgories = Category.objects.get(pk=id)
            catgories.delete()
            pass
        except Exception as ex:
            print(ex)
        return redirect('category')
    else:
        return render(request,'404.html')
def editCat(request, id):
    if request.user.isAdmin:
        try:
            categories = Category.objects.get(pk=id)
            context={
                'cats': categories
            }
        except Exception as ex:
            print(ex)
        return render(request, 'Category/editCategory.html', context)
    else:
        return render(request,'404.html')
def updateCat(request, id):
    if request.user.isAdmin:
        try:
                categories = Category()
                categories.id = id
                categories.name = request.POST['name']
                categories.image_path = request.FILES['image_path']
                categories.desc = request.POST['desc']
                categories.save()
                messages.success(request, 'Update Category Successfully')
        except Exception as ex:
            print(ex)
        return redirect(category)
    else:
        return render(request,'404.html')