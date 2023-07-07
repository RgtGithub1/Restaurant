import pytz
from django.utils import timezone
import logging


def cart_quantity(food_details_list, cart):
    try:
        for food in food_details_list:
            keys = cart.keys()
            total_quantity_price = 0
            for food in food_details_list:
                for id in keys:
                    if id == food.name:
                        total_quantity_price = total_quantity_price\
                                                      + cart.get(id) * \
                                                      food.price
            return total_quantity_price
    except Exception as e:
        logging.error(f"{e}")


def fetch_date_time():
    try:
        india_tz = pytz.timezone('Asia/Kolkata')
        india_time = timezone.now().astimezone(india_tz)
        format_date_time = india_time.strftime("%Y-%m-%d %H:%M:%S")
        return format_date_time
    except Exception as e:
        logging.error(f"{e}")
