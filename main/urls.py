from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('kids/', views.kids, name='kids'),
    path('products/', views.products, name='products'),
    path('sales/', views.sales, name='sales'),
    path("login/", views.login_request, name="login"),
    path('administration/', views.administration, name='admin'),
    path("register/", views.register_request, name="register"),
]
