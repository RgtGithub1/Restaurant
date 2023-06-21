from django import template

register = template.Library()

# @register.filter(name='is_in_cart')
# def is_in_cart(food, cart):
#     keys = cart.keys()
#     # print(keys)
#     print(food, cart)
#     return True

@register.filter(name='is_in_cart')
def is_in_cart(food, cart):
    keys = cart.keys()
    
    for id in keys:
        if id == str(food.id):
            print("food.id:", food.id)
            print("Food img:", food.image)
            print("Food name:", food.name)
            return True
    return False
   