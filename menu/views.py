from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, FoodItem, UserDetails
from django.contrib.auth.forms import UserCreationForm

def menu_list(request):
    # if not request.session.get('cart'):
    #     request.session['cart'] = {}
    
    # if not request.session.get('wish_list'):
    #     request.session['wish_list'] = {}
    categories = Menu.objects.all()

    cart = request.session.get('cart')
    keys = [int(key) for key in cart.keys()]
    list_quantity = FoodItem.objects.filter(id__in=keys)
    return render(request, 
                  'main_menu.html', 
                  {'categories': categories,
                   'list_quantity':list_quantity})

def food_items_details(request, id, menu_slug):
    print('entering into food_items_details')
    category = get_object_or_404(Menu, id=id)
    if request.method == 'POST':
        cart = request.session.get('cart')
        wish_list = request.session.get('wish_list')
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        quantity = request.POST.get('quantity')
        food_wish_list = request.POST.get('food_wish_list')

        if food_wish_list != 'this is wish':
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
        else:
            print('entering into else part of wish_list')
            wish_list[product] = 1

        request.session['cart'] = cart
        request.session['wish_list'] = wish_list
    cart = request.session.get('cart')
    keys = [int(key) for key in cart.keys()]
    list_quantity = FoodItem.objects.filter(id__in=keys)
    
    food_details_list = FoodItem.objects.filter(category_id=str(id))
    return render(request,
                  'food_details.html',
                  {'food_details_list': food_details_list,
                   'category': category,
                   'list_quantity': list_quantity
                   },
                   )


def cart(request):
    cart = request.session.get('cart')
    if request.method == 'POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        quantity = request.POST.get('quantity')
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
    
    request.session['cart'] = cart
    keys = [int(key) for key in cart.keys()]
    food_details_list = FoodItem.objects.filter(id__in=keys)
    return render(request, 'cart.html', {'food_details_list': food_details_list})


def wishlist(request):
    wish_list = request.session.get('wish_list')
    cart = request.session.get('cart')
    if request.method == 'POST':
        product = request.POST.get('product')
        wish_list.pop(product)
        cart[product] = 1

    request.session['cart'] = cart
    request.session['wish_list'] = wish_list
    keys = [int(key) for key in wish_list.keys()]
    food_details_list = FoodItem.objects.filter(id__in=keys)
    return render(request, 'wishlist.html', {'food_details_list': food_details_list})


def checkout(request):
    cart = request.session.get('cart')
    if request.method == 'POST':
        cart.clear()
    request.session['cart'] = cart
    return render(request, 'checkout.html')

# def signup(request):
#     # form = UserCreationForm()

#     return render(request, 'signup.html')

def signup(request):
    print('entering into signup page without post method')
    if request.method == 'POST':
        print('entering into signup page')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')
        print('first_name:',first_name)
        print('last_name:',last_name)
        print('contact_number:',contact_number)
        

        signup = UserDetails()
        signup.first_name = first_name
        signup.last_name = last_name
        signup.contact_number = contact_number
        signup.save()
        print('failed to insert')

        if not request.session.get('cart'):
            request.session['cart'] = {}
        
        if not request.session.get('wish_list'):
            request.session['wish_list'] = {}
        categories = Menu.objects.all()

        cart = request.session.get('cart')
        keys = [int(key) for key in cart.keys()]
        list_quantity = FoodItem.objects.filter(id__in=keys)
        return render(request, 
                    'main_menu.html', 
                    {'categories': categories,
                    'list_quantity':list_quantity})
    
    return render(request, 'signup.html')
