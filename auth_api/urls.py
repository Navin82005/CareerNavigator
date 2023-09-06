from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView, name='LoginView'),
    path('check/', authenticateLogin),
    path('signup/', SignupView),
    path('register/', authenticateRegister),
]
