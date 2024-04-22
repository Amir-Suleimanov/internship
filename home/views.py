
from django.shortcuts import get_object_or_404, render
from coffee_profile.models import CoffeeHouse


from coffee_profile.models import CoffeeHouse, Menu, MenuItem

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

def menu_detail(request, coffee_house_slug, menu_slug):
    menu = get_object_or_404(Menu, slug=menu_slug)
    menuitems = menu.menuitem_set.all()

    context = {
        'coffee_house_slug': coffee_house_slug,
        'menu': menu,
        'menuitems': menuitems
    }

    return  render(request, 'menu_slug.html', context)

def item_detail(request, coffee_house_slug, menu_slug, item_slug):
    item = get_object_or_404(MenuItem, slug=item_slug)

    context = {
        'coffee_house_slug': coffee_house_slug,
        'menu_slug': menu_slug,
        'item': item,
    }

    return  render(request, 'items_slug.html', context)


