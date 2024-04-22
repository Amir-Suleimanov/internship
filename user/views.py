from django.shortcuts import redirect, render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UsersForm

# Create your views here.

def Login(request):
    if request.method == 'POST':
        form = UsersForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home:home'))
    form = UsersForm()
    context= {
        'form': form
    }

    return render(request, 'auth.html', context)

def Logout(request):
    auth.logout(request)
    return redirect(reverse('home:home'))