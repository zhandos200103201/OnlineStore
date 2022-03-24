from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, ClothesForm, SalesForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import Clothes, Gift, Sales
from .forms import GiftForm


def all(request):
    clothes = Clothes.objects.all()
    gifts = Gift.objects.all()
    sales = Sales.objects.all()
    return render(request, 'main/All.html', {'clothes': clothes, "gifts": gifts, "sales": sales})


def about(request):
    return render(request, 'main/about.html')


def sales(request):
    sales = Sales.objects.all()
    return render(request, 'main/sales.html', {"sales": sales})


def kids(request):
    clothes = Clothes.objects.filter(category=2)
    return render(request, 'main/kids.html', {"clothes": clothes})


def products(request):
    gifts = Gift.objects.all()
    return render(request, 'main/products.html', {"gifts": gifts})


def clothes_list(request):
    clothes = Clothes.objects.all()
    return render(request, 'main/admin.html', {
        'clothes': clothes
    })


def clothes_detail(request, id):
    context = {}

    # add the dictionary during initialization
    context["cloth"] = Clothes.objects.get(id=id)

    return render(request, "main/clothes_detail.html", context)


def remove(request, id):
    cloth = Clothes.objects.get(id=id)
    cloth.delete()
    return redirect('admin')


def edit(request, id):
    clothes = Clothes.objects.get(id=id)
    return render(request, 'main/clothes_update.html', {'cloth': clothes})


def clothes_update(request, id):
    cloth = Clothes.objects.get(id=id)
    form = ClothesForm(request.POST, instance=cloth)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin')
    return render(request, "main/clothes_update.html", {"cloth": cloth})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('admin')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('login')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def addClothes(request):
    form = ClothesForm(request.POST)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin')
        else:
            error = 'Форма была неправильной'
    return render(request, 'main/CreateClothes.html', {"form": form, "error": error})


def addBoxes(request):
    form = GiftForm(request.POST)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('all')
        else:
            error = 'Форма была неправильной'
    return render(request, 'main/CreateBoxes.html', {"form": form, "error": error})


def addSales(request):
    form = SalesForm(request.POST)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('all')
        else:
            error = 'Форма была неправильной'
    return render(request, 'main/CreateSales.html', {"form": form, "error": error})
