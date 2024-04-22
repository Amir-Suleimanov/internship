from django.shortcuts import get_object_or_404, render

from menu.forms import MenuForm
from menu.models import Menu, MenuItem

# Create your views here.

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

def add_menu(request, coffee_house_slug):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MenuForm()

    context = {'form': form}
    return render(request, 'menu_add.html', context)