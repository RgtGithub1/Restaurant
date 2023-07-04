from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, FoodItem, UserDetails
from django.contrib.auth.forms import UserCreationForm
import re
from django.contrib import messages
import datetime
from django.db.models import Q
from .update import cart_quantity, fetch_date_time
import pytz

def signup(request):
    # del request.session['admin_food_view']
    # request.session.save()
    if not request.session.get('cart'):
            request.session['cart'] = {}

    if not request.session.get('wish_list'):
        request.session['wish_list'] = {}
        
    if not request.session.get('coustmer_details'):
        request.session['coustmer_details'] = {}

    def validate_gmail_data(gmail_value):
        gmail_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
        if re.fullmatch(gmail_pattern, gmail_value) is None:
            return False
        return True

    def validate_contact_data(contact_value):
        contact_pattern = r'\b[0-9]+\b'
        if len(contact_value) == 10:
            if re.fullmatch(contact_pattern, contact_value) is None:
                return False
            else:
                if contact_value[0] in ['6','7','8','9']:
                    return True
                return False
        return False
        
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        contact_number = request.POST.get('contact_number')
        if validate_contact_data(contact_number) and validate_gmail_data(user_email):
            # indian_tz = pytz.timezone('Asia/Kolkata')
            # current_date = datetime.datetime.now(indian_tz)
            # format_date_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
            india_time = fetch_date_time()
            signup = UserDetails()
            signup.user_email = user_email
            signup.contact_number = contact_number
            signup.created = india_time
            signup.updated = india_time
            signup.save()
            categories = Menu.objects.all()
            cart = request.session.get('cart')
            keys = [key for key in cart.keys()]
            list_quantity = FoodItem.objects.filter(name__in=keys)
            coustmer_details = request.session.get('coustmer_details')
            coustmer_details['contact_number'] = contact_number
            coustmer_details['date'] = india_time
            request.session['coustmer_details'] = coustmer_details

            return render(request, 
                        'main_menu.html', 
                        {'categories': categories,
                        'list_quantity':list_quantity})
        else:
            messages.error(request, 'Please enter valid email or contact number')
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')

def menu_list(request):
    categories = Menu.objects.all()
    cart = request.session.get('cart')
    keys = [key for key in cart.keys()]
    list_quantity = FoodItem.objects.filter(name__in=keys)
    return render(request, 
                  'main_menu.html', 
                  {'categories': categories,
                   'list_quantity':list_quantity})

def food_items_details(request, id, menu_slug):
    category = get_object_or_404(Menu, id=id)
    # del request.session['cart']
    # request.session.save()
    if request.method == 'POST':
        wish_list = request.session.get('wish_list')
        cart = request.session.get('cart')        
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        quantity = request.POST.get('quantity')
        food_wish_list = request.POST.get('food_wish_list')
        product = product.split('-')
        if food_wish_list != 'this is wish':
                quantity = cart.get(product[1])
                if quantity:
                    if remove:
                        if quantity <=1:
                            cart.pop(product[1])
                        else:
                            cart[product[1]] = quantity-1
                    else:
                        cart[product[1]] = quantity+1
                else:
                    cart[product[1]] = 1
        else:
            wish_list[product[0]] = 1

        request.session['wish_list'] = wish_list
        request.session['cart'] = cart

    cart = request.session.get('cart')
    keys = [key for key in cart.keys()]
    list_quantity = FoodItem.objects.filter(name__in=keys)
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
        product = product.split('-')
        quantity = cart.get(product[1])
        print('this is quantity of cart in', quantity)
        if quantity:
            if remove:
                if quantity <=1:
                    cart.pop(product[1])
                else:
                    cart[product[1]] = quantity-1
            else:
                print('Entering into increase quantity')
                cart[product[1]] = quantity+1
        else:
            cart[product[1]] = 1
    request.session['cart'] = cart
    cart = request.session.get('cart')
    keys = [key for key in cart.keys()]
    food_details_list = FoodItem.objects.filter(name__in=keys)
    return render(request, 'cart.html', {'food_details_list': food_details_list})


def wishlist(request):
    wish_list = request.session.get('wish_list')
    cart = request.session.get('cart')

    if request.method == 'POST':
        product = request.POST.get('product')
        product = product.split('-')
        wish_list.pop(product[0])
        cart[product[1]] = 1

    request.session['wish_list'] = wish_list
    request.session['cart'] = cart
    keys = [int(key) for key in wish_list.keys()]
    food_details_list = FoodItem.objects.filter(id__in=keys)
    return render(request, 'wishlist.html', {'food_details_list': food_details_list})

def checkout(request):
    cart = request.session.get('cart')
    coustmer_details = request.session.get('coustmer_details')

    if request.method == 'POST':
        india_time = fetch_date_time()
        cart = request.session.get('cart')
        keys = [key for key in cart.keys()]
        food_details_list = FoodItem.objects.filter(name__in=keys)
        Total_price = cart_quantity(food_details_list, cart)
        update_row = UserDetails.objects.filter(Q(contact_number = coustmer_details['contact_number']) & Q(created = coustmer_details['date']))
        update_row.update(food_details=cart, table_number=1, food_status='Pending', total_price=Total_price, serv_status='Pending', updated=india_time)

    cart.clear()
    request.session['admin_food_view'] = cart

    return render(request, 'checkout.html')
