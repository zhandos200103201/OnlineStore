from django.contrib import admin
from .models import Category, Gender, Clothes, Sales, Gift
from django.utils.safestring import mark_safe

admin.site.register(Category)
admin.site.register(Gender)
# admin.site.register(Clothes)
admin.site.register(Sales)
admin.site.register(Gift)


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show', 'category', 'price', 'available', 'gender']
    list_filter = ['available', 'gender', 'category']
    list_editable = ['price', 'available']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image))
        return "None"

    image_show.__name__ = "Картинка"
