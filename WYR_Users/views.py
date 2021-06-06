from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('userIndex')
        else:
            messages.info(request, 'username or password wrong!')
    return render(request, 'user/user.html')

def logoutUser(request):
    logout(request)
    return redirect('user')

def register(request):
    # if request.method == 'POST':
        # new_first_name = request.POST.get('fname')
        # new_last_name = request.POST.get('lname')
        # new_email = request.POST.get('email')
        # new_username = request.POST.get('username')
        # new_password = request.POST.get('password')
        # print(new_first_name, new_last_name, 
        #       new_email, new_username, new_password)
        
    userForm = UserForm()
    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            # print(userForm.cleaned_data)
            user = User.objects.create_user(**userForm.cleaned_data)
            return redirect('user')
            
        else:
            print(userForm.errors)
    context = {'userForm': userForm}
    return render(request, 'user/register.html', context)

    