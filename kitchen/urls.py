from django.urls import path
from . import views
# from .middlewares.auth import auth_middleware



urlpatterns = [
    path('', views.signup, name='signup'),
    ]
