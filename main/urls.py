from django.urls import path
from . import views


urlpatterns = [
    path('', views.all, name='all'),
    path('about/', views.about, name='about'),
    path('kids/', views.kids, name='kids'),
    path('products/', views.products, name='products'),
    path('sales/', views.sales, name='sales'),
    path('login/', views.login_request, name="login"),
    path('register/', views.register_request, name="register"),
    path('administration/', views.clothes_list, name='admin'),
    path('addclothes/', views.addClothes, name='addclothes'),
    path('addboxes/', views.addBoxes, name='addboxes'),
    path('addsales/', views.addSales, name='addsales'),
    path('<id>/', views.clothes_detail, name='detail'),
    path('edit/<int:id>', views.edit),
    path('delete/<int:id>', views.remove),
    path('update/<int:id>', views.clothes_update, name='update'),
]
