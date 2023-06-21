from django.shortcuts import render, get_object_or_404
from .models import Menu, FoodItem, cart
from django.views import View
# from .forms import QuantityForm


# class index(View):
#     def post(self, request):
#         product = request.POST.get('product')
#         print(product)


# def menu_list(request):
#     categories = Menu.objects.all()
#     product = request.POST.get('product')
#     print(product)

#     return render(request, 
#                   'main_menu.html', 
#                   {'categories': categories})

def menu_list(request):
    categories = Menu.objects.all()
    #=================================Experiment=================
    food = request.POST.get('food')
    print("Product id", food)
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(food)
        if quantity:
            cart[food] = quantity+1
        else:
            cart[food] = 1
    else:
        cart = {}
        cart[food] = 1

    request.session['cart'] = cart
    print("cart:", request.session['cart'])
    
    #============================================================
    return render(request, 
                  'main_menu.html', 
                  {'categories': categories})

def get(self, request):
    products = None
    request.session.get('cart').clear()
    categories = Category.get_all_category()




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

#====================Modifying=======================
def wishlist(request):
    # Retrieve the cart items from session or database
    # cart_items = request.session.get('cart', {})
    # context = {'cart_items': cart_items}
    ids = list(request.session.get('cart').keys())
    ids_list = []
    for i in ids:
        if i != "null":
            ids_list.append(i)
            print("qqqqqqqqqqqqqqqqqqqqq:",ids_list)
            print("QQQQQQQQQQQQQQQQQ:",ids_list)
            # print("cccccccccccccccccccccccccccccccccccccccc",list(request.session.get('cart').keys()))
            wish_list_food_details_list = FoodItem.objects.filter(id__in=ids_list)
            print(type(id), type(ids))
            print("wish_list_food_details_list", wish_list_food_details_list)
            # products = Product.get_products_by_id(ids)
            print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            return render(request, 'wishlist.html', {'products': wish_list_food_details_list})
        else:
            print("Error")
#=========================================================




def update_quantity(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        quantity = request.POST.get('quantity')

        print(f"Food ID: {food_id}, Quantity: {quantity}")  # Print the quantity values

        return render(request, 'food_details.html')

        # Rest of your view logic

    # Redirect or render a response as needed

