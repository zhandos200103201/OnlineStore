from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Sales, Clothes, Gift
from django.forms import ModelForm, TextInput, Textarea


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class GiftForm(ModelForm):
    class Meta:
        model = Gift
        fields = ["gender", "include_description", "price", "available", "image"]
        widgets = {
            "available": forms.CheckboxInput(),
            "include_description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите что включает в себя подарок'
            }),
            "image": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
            "price": TextInput(attrs={
                'placeholder': 'price'
            }),
            "gender": forms.Select(),
        }


class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ["name", "gender", "category", "price", "available", "image"]
        widgets = {
            "available": forms.CheckboxInput(),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите имя'
            }),
            "slug": model.slug,
            "image": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
            "price": TextInput(attrs={
                'placeholder': 'price'
            }),
            "gender": forms.Select(),
            "category": forms.Select()
        }


class SalesForm(ModelForm):
    class Meta:
        model = Sales
        fields = ["name", "gender", "category", "old_price", "new_price", "available", "image"]
        widgets = {
            "available": forms.CheckboxInput(),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите имя'
            }),
            "image": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку на фото'
            }),
            "old_price": TextInput(attrs={
                'placeholder': 'old_price'
            }),
            "new_price": TextInput(attrs={
                'placeholder': 'new_price'
            }),
            "gender": forms.Select(),
            "category": forms.Select()
        }
