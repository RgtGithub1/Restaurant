from django.shortcuts import render, get_object_or_404
from .models import Menu, FoodItem
from .forms import QuantityForm

def menu_list(request):
    # category = None
    categories = Menu.objects.all()
    # products = FoodItem.objects.filter(available=True)

    

    # if category_slug:
    #     category = get_object_or_404(Menu,
    #                                  slug=category_slug)
    #     products = products.filter(category=category)

    # return render(request,
    #               'main_menu.html',
    #               {'category': category,
    #                'categories': categories,
    #                'products': products})

    return render(request,
                'main_menu.html',
                {
                'categories': categories})

def food_items_details(request, id, menu_slug):
    category = get_object_or_404(Menu, id=id)
    print('category:',category )
    food_details_list = FoodItem.objects.filter(category_id=str(id))
    return render(request,
                  'food_details.html',
                  {'food_details_list': food_details_list,
                   'category': category})

# def my_view(request):
#     form = QuantityForm()
#     return render(request, 'food_details.html', {'form': form})
                   

def my_view(request):
    return render(request, 'food_details.html')