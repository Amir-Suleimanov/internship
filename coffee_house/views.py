from django.shortcuts import get_object_or_404, render

from coffee_house.forms import CoffeeHouseForm

# from .models import CoffeeHouse
from django.shortcuts import redirect, render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CoffeeHouseForm, UsersForm
from .models import CoffeeHouse

# Create your views here.
def all_coffee_house(request):
    form = {}
    if CoffeeHouse.objects:
        form = CoffeeHouse.objects.all()
    context = {
        'form': form
    }
    return render(request, 'home.html', context)

def coffee_house_detail(request, coffee_house_slug):
    coffee_house = get_object_or_404(CoffeeHouse, slug=coffee_house_slug)
    menus = coffee_house.menu_set.all()
    menuitems = {}
    if menus:
        for menu in menus:
            items = menu.menuitem_set.all()
            menuitems[menu] = items
    context = {
        'coffee_house': coffee_house,
        'menus': menus,
        'menuitems': menuitems,
        'coffee_house_slug': coffee_house_slug
    }

    return render(request, 'coffee_slug.html', context)


def profile(request):
    form = {}
    
    if CoffeeHouse.objects:
        form = CoffeeHouse.objects.all()

    menuslugs = {}
    coffee_house_slugs = {}
    for coffee_house in form:
        menus = coffee_house.menu_set.all()
        if menus:
            for menu in menus:
                menuslugs[coffee_house.slug] = menu.slug
            coffee_house_slugs[coffee_house.slug] = coffee_house.slug

    
    coffee_form = CoffeeHouseForm()
    context = {
        'coffee_house_slugs': coffee_house_slugs,
        'menuslugs': menuslugs,
        'form': form,
        'coffee_form': coffee_form
    }

    return render(request, 'profile_auth.html', context)

# def coffee_profile(request):
    
def add_coffee_house(request):
    if request.method == 'POST':
        form = CoffeeHouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('coffee_house:home'))
        else:
            print(form)
    else:
        form = CoffeeHouseForm()

    return render(request, 'coffee_add.html', {'form': form})






# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UsersForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('coffee_house:home'))
    form = UsersForm()
    context= {
        'form': form
    }

    return render(request, 'auth.html', context)

def logout(request):
    auth.logout(request)
    return redirect(reverse('coffee_house:home'))

def delete_coffee_house(request, coffee_house_slug):
    coffee_house = get_object_or_404(CoffeeHouse, slug=coffee_house_slug)
    coffee_house.delete()
    return HttpResponseRedirect(reverse('coffee_house:home'))

def edit_coffee_house(request, coffee_house_slug):
    coffee_house = get_object_or_404(CoffeeHouse, slug=coffee_house_slug)
    if request.method == 'POST':
        form = CoffeeHouseForm(request.POST, instance=coffee_house)
        
        if form.is_valid():
            form.save()
            return redirect('coffee_house:home')
    else:
        form = CoffeeHouseForm(instance=coffee_house)

    context = {'form': form, 'coffee_house': coffee_house}
    return render(request, 'edit_coffee_house.html', context)