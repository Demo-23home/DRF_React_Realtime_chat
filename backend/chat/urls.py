from django.urls import path
from .views import *

urlpatterns = [
    path("users/", list_all_users),
]
