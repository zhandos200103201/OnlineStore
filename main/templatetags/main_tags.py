from django import template
from main.models import Clothes
register = template.Library()


@register.simple_tag(name='clothe_tags')
def get_clothes(filter=None):
    if not filter:
        return Clothes.objects.all()
    else:
        return Clothes.objects.filter(category=filter)


# @register.simple_tag('main/All.html')
# def show_clothes():
#     tags = Clothes.objects.all()
#     return {'tags': tags}

