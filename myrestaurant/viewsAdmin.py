from django.shortcuts import render,  redirect


def is_admin(request):
    if request.user.isAdmin:
        return True
    else:
        return False