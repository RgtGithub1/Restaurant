from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, FoodItem, cart
<<<<<<< HEAD
=======
from django.views import View
# from .forms import QuantityForm

>>>>>>> 3caf7150e6a6c7aed0c1e4491195e8dc11781e45

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
<<<<<<< HEAD
    return render(request, 
                  'main_menu.html', 
                  {'categories': categories})
=======
    #=================================Experiment=================
    product = request.POST.get('product')
    print("Product id", product)
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)
        if quantity:
            cart[product] = quantity+1
        else:
            cart[product] = 1

    else:
        cart = {}
        cart[product] = 1

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



>>>>>>> 3caf7150e6a6c7aed0c1e4491195e8dc11781e45

def food_items_details(request, id, menu_slug):
    print('entering into food_items_details')
    

    category = get_object_or_404(Menu, id=id)

    if request.method == 'POST':
        global cart
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        quantity = request.POST.get('quantity')
        # cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            print('entering into else part')
            cart = {}
            cart[product] = 1 


        request.session['cart'] = cart
        print('cart:', cart)


    print('category:', category)
    # print('cart:', cart)

    food_details_list = FoodItem.objects.filter(category_id=str(id))



    return render(request,
                  'food_details.html',
                  {'food_details_list': food_details_list,
                   'category': category
                   },
                   )



# def cart(request):
#     # print('cart in cart:', request.cart)
#     mail=request.session.get('cart')
#     print('mail',mail)

#     print('mail.keys:::',mail.values())

#     keys = [int(key) for key in mail.keys()]
#     food_details_list = FoodItem.objects.filter(id__in=keys)
#     print(food_details_list)
#     return render(request, 'cart.html',{'products' : food_details_list} )

def cart(request):
    mail = request.session.get('cart')
    keys = [int(key) for key in mail.keys()]
    food_details_list = FoodItem.objects.filter(id__in=keys)

    # Create a dictionary mapping FoodItem objects to their quantities
    product_quantity_dict = {food: mail[str(food.id)] for food in food_details_list}

    return render(request, 'cart.html', {'food_details_list': food_details_list, 'quantities': product_quantity_dict})


def wishlist(request):

    return render(request, 'wishlist.html')

