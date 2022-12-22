from django.urls import path
from .views import UserRegister, index, UserLogin, logout_user

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('', index, name='home'),
    path('logout/', logout_user, name='logout'),
]
