from django.forms import ModelForm
from django import forms
from .models import Category

class UploadCategory(ModelForm):
    name = forms.TextInput()
    image_path = forms.FileField()
    desc = forms.Textarea()
    class Meta:
        model = Category
        fields = ['name', 'image_path', 'desc']