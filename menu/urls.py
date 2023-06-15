from django.urls import path
from . import views


app_name = 'menu'
urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<int:id>/<slug:menu_slug>/', views.food_items_details, name='food_list_by_category'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('update/', views.update_quantity, name='update_quantity')
    ]
