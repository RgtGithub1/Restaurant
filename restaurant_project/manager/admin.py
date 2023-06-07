from django.contrib import admin
from .models import Coupon, EmployeeDetail


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code_name', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code_name']


@admin.register(EmployeeDetail)
class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'employee_role', 'active']
    list_filter = ['active']
    search_fields = ['employee_name']

