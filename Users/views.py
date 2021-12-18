from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
    return render(request,template_name='Users/form.html',context={'form':form})



def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pswd')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, template_name='Users/login.html', context={})


def logout_view(request):
    logout(request)
    return redirect('loginpage')


