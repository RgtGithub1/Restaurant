from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Menu, FoodItem, UserDetails
import re
from django.contrib import messages
from django.db.models import Q
from .update import cart_quantity, fetch_date_time
import logging
import os
# import requests as r
# import json


def signup(request):
    """
    Args:
        email (string): Enter email.
        contact number (string): Enter contact number.

    Returns:
        if enter email and contact number valid:
            it will render to menu page
        else:
            reverse to signup page.
    """

    # To delete any session refer below syntax
    # del request.session['session_name']
    # request.session.save()

    fect_path = os.path.normpath(os.getcwd())
    log_path = f"{fect_path}\\logs\\TableTap.log"
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format='%(filename)s:%(lineno)d - '
               '%(asctime)s - %(levelname)s - %(message)s')

    logging.info("Signup page")

    if 'cart' not in request.session:
        request.session['cart'] = {}
        logging.info("cart session created")

    if 'wish_list' not in request.session:
        request.session['wish_list'] = {}
        logging.info("Wish_list session created")

    if 'coustmer_details' not in request.session:
        request.session['coustmer_details'] = {}
        logging.info("coustmer_details session created")

    def validate_gmail_data(gmail_value):

        try:
            gmail_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
            if re.fullmatch(gmail_pattern, gmail_value) is None:
                return False
            return True
        except Exception as e:
            logging.error(f"{e}")

    def validate_contact_data(contact_value):
        try:
            contact_pattern = r'\b[0-9]+\b'
            if len(contact_value) == 10:
                if re.fullmatch(contact_pattern, contact_value) is None:
                    return False
                else:
                    if contact_value[0] in ['6', '7', '8', '9']:
                        return True
                    return False
            return False
        except Exception as e:
            logging.error(f"{e}")
    if request.method == 'POST':
        user_email = request.POST.get('user_email')
        contact_number = request.POST.get('contact_number')
        if validate_contact_data(contact_number) and \
                validate_gmail_data(user_email):
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
            logging.info("After sginup render to Menu page")
            return render(request,
                          'main_menu.html',
                          {'categories': categories,
                           'list_quantity': list_quantity})
        else:
            messages.error(request,
                           'Please enter valid email or contact number')
            logging.error("Please enter valid email or contact number")
            return redirect(reverse('menu:signup'))

    else:
        return render(request, 'signup.html')
        # return redirect(reverse('menu:signup'))


def menu_list(request):
    """
    This method display list of all food category on menu page
    and based on your select category, it will go category details page.

    """
    categories = Menu.objects.all()
    cart = request.session.get('cart')
    logging.info("Back to Menu page")
    keys = [key for key in cart.keys()]
    list_quantity = FoodItem.objects.filter(name__in=keys)
    return render(request,
                  'main_menu.html',
                  {'categories': categories,
                   'list_quantity': list_quantity})


def food_items_details(request, id, menu_slug):
    """
    This method display selected category food details on menu page

    cart: if you click on cart button food will store in cart session
        if you click on + button, selected food quantity increase by 1 in cart
        if you click on - button, selected food quantity decrease by 1 in cart

    wishlist: if you click on wishlist button
                food will store in wishlist session.

    """
    category = get_object_or_404(Menu, id=id)
    logging.info(f"Selected {menu_slug}")
    if request.method == 'POST':
        # Process the form data
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
                    if quantity <= 1:
                        cart.pop(product[1])
                        logging.info(f"{product[1]} removed from cart")
                    else:
                        cart[product[1]] = quantity - 1
                        logging.info(
                            f"{product[1]} decreased one quantity from cart")
                else:
                    cart[product[1]] = quantity + 1
                    logging.info(
                        f"{product[1]} increased one quantity in cart")
            else:
                cart[product[1]] = 1
                logging.info(f"{product[1]} added to cart")
        else:
            wish_list[product[0]] = 1
            logging.info(f"{product[0]} added to wishlist")

        request.session['wish_list'] = wish_list
        request.session['cart'] = cart
        cart = request.session.get('cart')

        # Redirect to the same view using the reverse function
        return redirect(reverse(
            'menu:food_items_details',
            kwargs={'id': id, 'menu_slug': menu_slug}))

    cart = request.session.get('cart')
    keys = [key for key in cart.keys()]
    list_quantity = FoodItem.objects.filter(name__in=keys)
    food_details_list = FoodItem.objects.filter(category_id=str(id))
    return render(request,
                  'food_details.html',
                  {'food_details_list': food_details_list,
                   'category': category,
                   'list_quantity': list_quantity})


def cart(request):
    """
    This method display all food details which are store in cart.

    if you click on + button, selected food quantity increase by 1 in cart
    if you click on - button, selected food quantity decrease by 1 in cart

    """
    logging.info("Cart page fetched")
    cart = request.session.get('cart')

    if request.method == 'POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        quantity = request.POST.get('quantity')
        product = product.split('-')
        quantity = cart.get(product[1])
        if quantity:
            if remove:
                if quantity <= 1:
                    cart.pop(product[1])
                    logging.info(f"{product[1]} removed from cart")
                else:
                    cart[product[1]] = quantity-1
                    logging.info(
                        f"{product[1]} decreased one quantity from cart")
            else:
                cart[product[1]] = quantity+1
                logging.info(f"{product[1]} increased one quantity in cart")
        else:
            cart[product[1]] = 1

        request.session['cart'] = cart
        return redirect(reverse('menu:cart'))

    cart = request.session.get('cart')
    keys = [key for key in cart.keys()]
    food_details_list = FoodItem.objects.filter(name__in=keys)
    return render(request,
                  'cart.html',
                  {'food_details_list': food_details_list})


def wishlist(request):
    """
    This method display all food details which are store in wishlist.

    if you click on add to cart button:
        selected food will store in cart and default quantity as 1

    """
    logging.info("wishlist page fetched")
    wish_list = request.session.get('wish_list')
    cart = request.session.get('cart')

    if request.method == 'POST':
        product = request.POST.get('product')
        product = product.split('-')
        print('product is:', product)
        logging.info(f"{product[1]} added to cart from wishlist")
        wish_list.pop(product[0])
        cart[product[1]] = 1
        request.session['wish_list'] = wish_list
        request.session['cart'] = cart

    wish_list = request.session.get('wish_list')
    keys = [int(key) for key in wish_list.keys()]
    food_details_list = FoodItem.objects.filter(id__in=keys)
    return render(request,
                  'wishlist.html',
                  {'food_details_list': food_details_list})


def checkout(request):
    """
    This method display food status to user.

    if food status in DB is pending:
        status is food is preparing
    else:
        food is ready
    """
    logging.info("Checkout page fetched")
    cart = request.session.get('cart')
    coustmer_details = request.session.get('coustmer_details')
    if request.method == 'POST':
        india_time = fetch_date_time()
        cart = request.session.get('cart')
        keys = [key for key in cart.keys()]
        food_details_list = FoodItem.objects.filter(name__in=keys)
        Total_price = cart_quantity(food_details_list, cart)
        update_row = UserDetails.objects.filter(
            Q(contact_number=coustmer_details['contact_number'])
            & Q(created=coustmer_details['date']))
        update_row.update(food_details=cart,
                          table_number=1,
                          food_status='Pending',
                          total_price=Total_price,
                          serv_status='Pending',
                          updated=india_time)
        logging.info("order placed")
        return redirect(reverse('menu:checkout'))
        # try:
        #     # from sinch account:
        #     SERVICE_PLAN_ID = "bf296a6b335c47fb9fe4bfcfa9066b33"
        #     access_token = "60c70ea0e08e48ffaff4a2fd9a9e3eeb"
        #     from_ = "447520650698"
        #     message = 'This is demo message! by sinch account'
        #     to_ = "917975759756"
        #     headers = {
        #         "Authorization": f"Bearer {access_token}",
        #         "Content-Type": "application/json"
        #     }
        #     payload = {
        #         "from": from_,
        #         "to": [to_],
        #         "body": message
        #     }
        #     response = r.post(
        #         f'https://sms.api.sinch.com/xms/v1/{SERVICE_PLAN_ID}/batches',
        #         headers=headers,
        #         data=json.dumps(payload)
        #     )
        #     if response.status_code == 201:
        #         print('SMS sent successfully to multiple numbers.')
        #     else:
        #         print('Failed to send SMS to multiple numbers. Error:',
        #               response.text)
        #         print('response code is:', response.status_code)
        #     logging.info("order placed")
        #     return redirect(reverse('menu:checkout'))
        # except Exception as e:
        #     logging.error(f"{e}")
        #     return redirect(reverse('menu:checkout'))
    cart.clear()
    request.session['cart'] = cart

    return render(request, 'checkout.html')
