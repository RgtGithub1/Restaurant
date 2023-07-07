import pytz
from django.utils import timezone


def cart_quantity(food_details_list, cart):
    for food in food_details_list:
        keys = cart.keys()
        total_amount_quantity_price = 0
        for food in food_details_list:
            for id in keys:
                if id == food.name:
                    total_amount_quantity_price = total_amount_quantity_price\
                                                  + cart.get(id) * food.price
        return total_amount_quantity_price


def fetch_date_time():
    india_tz = pytz.timezone('Asia/Kolkata')
    india_time = timezone.now().astimezone(india_tz)
    format_date_time = india_time.strftime("%Y-%m-%d %H:%M:%S")
    return format_date_time
