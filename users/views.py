from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

#! Birden fazla authentication backend'i olduğu için, hangi backendi kullanacağını belirtmeliyiz.`backend` parametresini eklemek için import edildi. 2. Yol;
from django.contrib.auth import get_backends

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def register(request):
    form_user = UserForm
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            user = form_user.save()
            
            #! Birden fazla authentication backend'i olduğu için, hangi backendi kullanacağını belirtiyoruz. `backend` parametresini ekliyoruz. Aynısını user_loginde de yapmalıyız eğer çalışmazsa. 1. Yol;
            login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')

            #! Birden fazla authentication backend'i olduğu için, hangi backendi kullanacağını belirtiyoruz. 2. Yol;
            """
            backend = get_backends()[0]  # İlk backend'i kullanabilirsiniz
            backend_path = f"{backend.__module__}.{backend.__class__.__name__}"
            login(request, user, backend=backend_path)
            """

            
            # login(request, user)
            messages.success(request, 'You have been registered')
            return redirect('home')
    context = {
        'form_user': form_user
    }
    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user() #! formdan gelen user bilgileri alıyoruz.
        login(request, user) #! Gelen user bilgileri ile login isteği yapıyoruz.
        messages.success(request, "You have been logged in.")
        return redirect('home')
    return render(request, 'users/login.html', {"form": form})
    #! context içindeki veriyi buradan da gönderebiliriz.

def user_logout(request):
    messages.success(request, "You have been logged out.")
    logout(request)
    return redirect('home')
    # return render(request, 'users/logout.html')
    #! Eğer bir logout template'i istenirse yazılabilir. Ancak gerek yok.
    