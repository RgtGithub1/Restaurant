from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, FoodItem, cart

def menu_list(request):
    categories = Menu.objects.all()
    return render(request, 
                  'main_menu.html', 
                  {'categories': categories})

def food_items_details(request, id, menu_slug):
    print('entering into food_items_details')
    

    category = get_object_or_404(Menu, id=id)

    if request.method == 'POST':
        cart = request.session.get('cart')
        if not cart:
            print('entering into not cart condition')
            request.session['cart'] = {}
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        increase = request.POST.get('increase')
        quantity = request.POST.get('quantity')
        print('product',product)
        print('remove',remove)
        print('quantity',quantity)
        print('increase',increase)
        



        # cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    print('entering into remove condition')
                    if quantity <=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    print('entering into increase condition')
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            print('entering into else part')
            cart = {}
            cart[product] = 1 


        request.session['cart'] = cart
        # print('cart:', cart)


    # print('category:', category)
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
    cart = request.session.get('cart')
    if request.method == 'POST':
        product = request.POST.get('product')
        print('product from cart is:', product)
        if product:
            cart.pop(product)
        else:
            cart.clear()
    
    request.session['cart'] = cart
    keys = [int(key) for key in cart.keys()]
    food_details_list = FoodItem.objects.filter(id__in=keys)

    # Create a dictionary mapping FoodItem objects to their quantities
    # product_quantity_dict = {food: cart[str(food.id)] for food in food_details_list}

    return render(request, 'cart.html', {'food_details_list': food_details_list})


def wishlist(request):

    return render(request, 'wishlist.html')

