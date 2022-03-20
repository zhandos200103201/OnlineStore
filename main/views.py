from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate


def administration(request):
    return render(request, 'main/admin.html')


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def cart(request):
    return render(request, 'main/cart.html')


def sales(request):
    return render(request, 'main/sales.html')


def kids(request):
    return render(request, 'main/kids.html')


def products(request):
    return render(request, 'main/products.html')


def dashboard(request):
    return render(request, 'main/dashboard.html')


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
