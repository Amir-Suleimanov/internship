from django.shortcuts import redirect, render
from django.urls import reverse

from .models import CoffeeHouse
from .forms import CoffeeHouseForm, MenuForm
# Create your views here.

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
    
def coffeehouse_create(request):
    if request.method == 'POST':
        form = CoffeeHouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('coffee_profile:profile'))
    else:
        form = CoffeeHouseForm()

    return render(request, 'profile_auth.html', {'form': form})


def add_menu(request, coffee_house_slug):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MenuForm()

    context = {'form': form}
    return render(request, 'add_menu.html', context)