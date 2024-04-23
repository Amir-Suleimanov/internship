from audioop import reverse
from django.shortcuts import get_object_or_404, redirect, render

from menu.forms import MenuForm, MenuItemForm
from menu.models import Menu, MenuItem
from pytils.translit import slugify

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
def item_detail(request, coffee_house_slug, menu_slug, item_id):
    item = get_object_or_404(MenuItem, id=item_id)

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
            menu = form.save(commit=False)
            menu.slug = slugify(menu.name)
            menu.save()
            return redirect('menu:menu_detail', coffee_house_slug, menu.slug)
    else:
        form = MenuForm()

    context = {'form': form, 'coffee_house_slug': coffee_house_slug, }
    return render(request, 'add_menu.html', context)


def edit_menu(request, coffee_house_slug, menu_slug):
    menu = get_object_or_404(Menu, slug=menu_slug)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            print('Зашло 2')
            form.save()
            return redirect('menu:menu_detail', coffee_house_slug=coffee_house_slug, menu_slug=menu_slug)
    else:
        form = MenuForm(instance=menu)
    context = {
        'slugs': (coffee_house_slug, menu_slug),
        'form': form,
        'menu': menu,
        }
    print(menu.coffee_house)
    return render(request, 'edit_menu.html', context)


def delete_menu(request, coffee_house_slug, menu_slug):
    menu = get_object_or_404(Menu, slug=menu_slug)
    menu.delete()
    return redirect('coffee_house:coffee_house_detail', coffee_house_slug=coffee_house_slug)


def item_add(request, coffee_house_slug, menu_slug):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu:menu_detail', coffee_house_slug=coffee_house_slug, menu_slug=menu_slug)
    else:
        form = MenuItemForm()

    context = {'form': form, 'slugs' : (coffee_house_slug, menu_slug)}
    return render(request, 'item_add.html', context)


def item_edit(request, coffee_house_slug, menu_slug, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu:menu_detail', coffee_house_slug=coffee_house_slug, menu_slug=menu_slug)
    else:
        form = MenuItemForm(instance=item)
    item.quantity = int(item.quantity)
    context = {
        'slugs': (coffee_house_slug, menu_slug),
        'form': form,
        'item': item,
        }
    
    return render(request, 'edit_item.html', context)

def delete_item(request, coffee_house_slug, menu_slug, item_id):
    menu = get_object_or_404(MenuItem, id=item_id)
    menu.delete()
    return redirect('menu:menu_detail', coffee_house_slug=coffee_house_slug, menu_slug=menu_slug)