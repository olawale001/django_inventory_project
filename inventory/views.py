from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Item, Ingredient, Order, Sale
from .forms import ItemForm, IngredientForm, OrderForm

def index(request):
    return render(request, 'inventory/index.html')

def inventory_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})

def inventory_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'inventory/inventory_detail.html', {'item': item})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'inventory/login.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'inventory/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def dashboard(request):
    return render(request, 'inventory/dashboard.html')

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = ItemForm()
    return render(request, 'inventory/inventory_form.html', {'form': form})

@login_required
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory_detail', pk=pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'inventory/inventory_form.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory_list')
    return render(request, 'inventory/inventory_confirm_delete.html', {'item': item})


@login_required
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})

@login_required
def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm()
    return render(request, 'inventory/ingredient_form.html', {'form': form})

@login_required
def update_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient_list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'inventory/ingredient_form.html', {'form': form})

@login_required
def delete_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient_list')
    return render(request, 'inventory/ingredient_confirm_delete.html', {'ingredient': ingredient})

@login_required
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'inventory/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'inventory/order_detail.html', {'order': order})

@login_required
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'inventory/order_form.html', {'form': form})

@login_required
def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'inventory/sales_list.html', {'sales': sales})