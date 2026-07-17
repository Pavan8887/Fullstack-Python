from django.shortcuts import redirect, render
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib import messages
# Create your views here.

from .forms import LoginForm
import login

def login_view(request):
    form = LoginForm(request,data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.sucess(request,f'welcome back,{user.username}!')
            return redirect('book_list')
        else:
            messages.error(request,'invalid username or password.')
    return render(request, 'acconys/login.html',{'form ':form})

def logout_view(request):
    logout(request) 
    return redirect('login')