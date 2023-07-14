from django.urls import path
from . import views
# from .middlewares.auth import auth_middleware


app_name = 'kitchen'
urlpatterns = [
    path('', views.kitchen_home_page, name='kitchen_home_page'),
    ]
