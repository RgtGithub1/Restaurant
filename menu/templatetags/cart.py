from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(food  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == food.id:
            return True
    return False


@register.filter(name='cart_quantity')
def cart_quantity(food  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == food.id:
            return cart.get(id)
    return 0

@register.filter(name='quantity_price')
def cart_quantity(food  , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == food.id:
            amount_quantity_price = cart.get(id) * food.price
            return amount_quantity_price
    return 0

@register.filter(name='total_price')
def cart_quantity(food_details_list  , cart):
    print('entering into total_price')
    for food in food_details_list:
        keys = cart.keys()
        total_amount_quantity_price = 0
        for food in food_details_list:
            for id in keys:
                if int(id) == food.id:
                    total_amount_quantity_price = total_amount_quantity_price + cart.get(id) * food.price
        return total_amount_quantity_price
    
@register.filter(name='total_quantity')
def cart_quantity(food_details_list  , cart):
    print('entering into total_quantity')
    for food in food_details_list:
        keys = cart.keys()
        total_quantity_price = 0
        for food in food_details_list:
            for id in keys:
                if int(id) == food.id:
                    total_quantity_price = total_quantity_price + cart.get(id)
        return total_quantity_price

@register.filter(name='list_quantity_detail')
def cart_quantity(list_quantity  , cart):
    print('entering into list_quantity_detail',list_quantity)

    for food in list_quantity:
        keys = cart.keys()
        total_quantity_price = 0
        for food in list_quantity:
            for id in keys:
                if int(id) == food.id:
                    total_quantity_price = total_quantity_price + cart.get(id)
        return total_quantity_price
    return 0
