from django.shortcuts import render
from menu.models import UserDetails
from django.db.models import Q


# Create your views here.
def kitchen_home_page(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        update_kitchen_food = UserDetails.objects.filter(id = int(product))
        update_kitchen_food.update(food_status = 'Done')
        
    order_details_id = UserDetails.objects.filter(food_status = 'Pending')
    return render(request, 
                'kitchen.html',
                {'order_details_id':order_details_id})