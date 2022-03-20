from django.contrib import admin
from .models import Category, Gender, Clothes


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
