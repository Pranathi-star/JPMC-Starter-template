from django.urls import path, include
from .views import *
from .api import SimpleApI

urlpatterns = [
    path('login/', login),
    path('register/student/', register_user),

]