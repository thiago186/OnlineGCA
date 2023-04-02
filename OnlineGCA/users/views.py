from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def CreateUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Username created sucessfully!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/CreateUser.html', {'form': form})

@login_required
def ProfilePage(request):
    return render(request, 'users/ProfilePage.html')