from django import template
import ast
from menu.models import FoodItem, UserDetails
from django.db.models import Q
import logging


register = template.Library()

# ------------------------Menu app--------------------
# 1) Below function used in food_details.html


@register.filter(name='is_in_cart')
def is_in_cart(food, cart):
    """
    This method
    return True:
            when food is store in cart
    else:
        return False
    """
    try:
        keys = cart.keys()
        for id in keys:
            if id == food.name:
                return True
        return False
    except Exception as e:
        logging.error(f"{e}")

# 2) Below functions are used in cart.html
# also used in kitchen.html, food_details.html


@register.filter(name='food_quantity')
def food_quantity(food, cart):
    """
    This method return selected food quantity.
    """
    try:
        if type(cart) == str:
            cart = ast.literal_eval(cart)
        keys = cart.keys()
        for id in keys:
            if id == food.name:
                return cart.get(id)
        return 0
    except Exception as e:
        logging.error(f"{e}")


@register.filter(name='food_quantity_price')
def food_quantity_price(food, cart):
    """
    This method return total price of food quantity.
    """
    try:
        keys = cart.keys()
        for id in keys:
            if id == food.name:
                quantity_price = cart.get(id) * food.price
                return quantity_price
        return 0
    except Exception as e:
        logging.error(f"{e}")


@register.filter(name='cart_total_price')
def cart_total_price(food_details_list, cart):
    """
    This method return Total price of cart.
    """
    try:
        for food in food_details_list:
            keys = cart.keys()
            total_price = 0
            for food in food_details_list:
                for id in keys:
                    if id == food.name:
                        total_price = total_price + cart.get(id) * food.price
            return total_price
    except Exception as e:
        logging.error(f"{e}")


@register.filter(name='cart_total_quantity')  # also used in project_base.html
def cart_total_quantity(food_details_list, cart):
    """
    This method return total quantity of cart.
    """
    try:
        for food in food_details_list:
            keys = cart.keys()
            total_quantity = 0
            for food in food_details_list:
                for id in keys:
                    if id == food.name:
                        total_quantity = total_quantity + cart.get(id)
            return total_quantity
        return 0
    except Exception as e:
        logging.error(f"{e}")

# 3) Below function used in checkout.html


@register.filter(name='food_status')
def food_status(coustmer_details):
    """
    This method return food status.
    """
    try:
        food_status_update = UserDetails.objects.filter(
            Q(contact_number=coustmer_details['contact_number']) &
            Q(created=coustmer_details['date']))
        for status in food_status_update:
            pass
        if status.food_status == 'Done':
            return 'Food is ready'
        else:
            return 'Food is preparing'
    except Exception as e:
        logging.error(f"{e}")

# ------------------------Kitchen app-----------------------
# 1) Below function used in Kitchen.html


@register.filter(name='kitchen_order_details')
def kitchen_order_details(food_details):
    """
    This method return food order details to prepare food.
    """
    try:
        print('food_details is', food_details)
        food_details = ast.literal_eval(food_details)
        keys = [key for key in food_details.keys()]
        food_details_list = FoodItem.objects.filter(name__in=keys)
        return food_details_list
    except Exception as e:
        logging.error(f"{e}")
