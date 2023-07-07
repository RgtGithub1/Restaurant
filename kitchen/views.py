from django.shortcuts import render, redirect
from menu.models import UserDetails
from django.db.models import Q
from django.urls import reverse


# Create your views here.
def kitchen_home_page(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        update_kitchen_food = UserDetails.objects.filter(id = int(product))
        update_kitchen_food.update(food_status = 'Done')
        return redirect(reverse('kitchen:kitchen_home_page'))
        # update_kitchen_food.save()
        
    order_details_id = UserDetails.objects.filter(food_status = 'Pending')
    return render(request, 
                'kitchen.html',
                {'order_details_id':order_details_id})