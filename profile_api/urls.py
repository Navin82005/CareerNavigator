from django.urls import path
from .views import *

urlpatterns = [
    path('<str:id>', ProfileView, name='profile'),
]
