from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import MyUser

def index(request):
    users = MyUser.objects.all()
    
    ctx = {
            'users': users,      
    }
    return render(request, 'register/index.html', ctx)

class UserRegister(CreateView):
    form_class = UserRegisterForm
    template_name = 'register/registr.html'

class UserLogin(LoginView):
    template_name = 'register/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')
