from django.shortcuts import render, get_object_or_404
from .models import Menu, FoodItem

def menu_list(request, category_slug=None):
    category = None
    categories = Menu.objects.all()
    products = FoodItem.objects.filter(available=True)

    # if category_slug:
    #     category = get_object_or_404(Menu,
    #                                  slug=category_slug)
    #     products = products.filter(category=category)

    return render(request,
                  'demo.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

    # return render(request,
    #             'Main_menu.html',
    #             {'category': category,
    #             'categories': categories,
    #             'products': products})
