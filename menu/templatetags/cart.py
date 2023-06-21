from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(food  , cart):
    print('entering into is_in_cart', food.id, cart)
    keys = cart.keys()
    # print('keys:',keys)
    for id in keys:
        print(type(id),type(food.id))
        print(id, food.id)
        if int(id) == food.id:
            print('true')
            return True
    print('false')
    return False


@register.filter(name='cart_quantity')
def cart_quantity(food  , cart):
    # print('entering into cart_quantity')
    keys = cart.keys()
    for id in keys:
        if int(id) == food.id:
            return cart.get(id)
    return 0;

@register.filter(name='quantity_price')
def cart_quantity(food  , cart):
    # print('entering into cart_quantity')
    keys = cart.keys()
    print('keys:',keys)
    for id in keys:
        if int(id) == food.id:
            amount_quantity_price = cart.get(id) * food.price
            return amount_quantity_price
    return 0;

@register.filter(name='total_price')
def cart_quantity(food_details_list  , cart):
    for food in food_details_list:
    # print('entering into cart_quantity')
        keys = cart.keys()
        amount_quantity_price1 = 0
        for food in food_details_list:
            for id in keys:
                if int(id) == food.id:
                    amount_quantity_price1 = amount_quantity_price1 + cart.get(id) * food.price
        return amount_quantity_price1
