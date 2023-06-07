from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'table_number', 'first_name', 'last_name', 'payment_id', 'payment_type', 'paid',
                    'food_name', 'quantity', 'food_price','coupon_name','coupon_discount','coupon_amount',
                    'total_food_price', 'created', 'updated']
    # list_filter = ['created', 'updated']

