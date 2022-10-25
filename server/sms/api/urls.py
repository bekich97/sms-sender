from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create, name="create"),
    path('user-info/', user_info, name="user-info")
]