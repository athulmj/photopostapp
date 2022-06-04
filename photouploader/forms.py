from django.db import models
from django.forms import fields
from .models import ImageUpload
from django import forms


class UserImageForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = '__all__'

        widgets = {
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "caption": forms.TextInput(attrs={"class": "form-control"})
        }