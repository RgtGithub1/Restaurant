def cart_quantity(food_details_list  , cart):
    for food in food_details_list:
        keys = cart.keys()
        total_amount_quantity_price = 0
        for food in food_details_list:
            for id in keys:
                if int(id) == food.id:
                    total_amount_quantity_price = total_amount_quantity_price + cart.get(id) * food.price
        return total_amount_quantity_price
    