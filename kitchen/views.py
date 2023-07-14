from django.shortcuts import render, redirect
from menu.models import UserDetails
from django.db.models import Q
from django.urls import reverse
import logging


# Create your views here.
def kitchen_home_page(request):
    '''This method shows food is ready or not, after food generation need to it will update as food is prepared'''
    try:
        if request.method == 'POST':
            product = request.POST.get('product')
            update_kitchen_food = UserDetails.objects.filter(id = int(product))
            update_kitchen_food.update(food_status = 'Done')
            logging.info("Food prepared")
            return redirect(reverse('kitchen:kitchen_home_page'))
            
        order_details_id = UserDetails.objects.filter(food_status = 'Pending')
        return render(request, 
                    'kitchen.html',
                    {'order_details_id':order_details_id})
    except Exception as e:
        logging.error(f"kitchen_home_page method have an issue:{e}")