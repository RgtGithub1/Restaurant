from django.shortcuts import render, get_object_or_404
from .models import Menu, FoodItem, cart
# from .forms import QuantityForm



def menu_list(request):
    categories = Menu.objects.all()
    return render(request, 
                  'main_menu.html', 
                  {'categories': categories})


def food_items_details(request, id, menu_slug):
    category = get_object_or_404(Menu, id=id)
    print('category:', category)
    food_details_list = FoodItem.objects.filter(category_id=str(id))
    return render(request,
                  'food_details.html',
                  {'food_details_list': food_details_list,
                   'category': category})


def cart(request):
    # Retrieve the cart items from session or database
    # cart_items = cart.objects.all()
    # print("cart_items::::",cart_items)
    cart_items = request.session.get('cart', {})
    context = {'cart_items': cart_items}
    return render(request, 'cart.html', context)

def wishlist(request):
    # Retrieve the cart items from session or database
    cart_items = request.session.get('cart', {})
    context = {'cart_items': cart_items}
    return render(request, 'wishlist.html', context)




def update_quantity(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        quantity = request.POST.get('quantity')

        print(f"Food ID: {food_id}, Quantity: {quantity}")  # Print the quantity values

        return render(request, 'food_details.html')

        # Rest of your view logic

    # Redirect or render a response as needed

