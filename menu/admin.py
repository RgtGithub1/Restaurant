from django.contrib import admin
from .models import Menu, FoodItem, UserDetails


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available',
                    'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(UserDetails)
class UserDetails(admin.ModelAdmin):
    list_display = ['id','contact_number','table_number','food_details','total_price']

