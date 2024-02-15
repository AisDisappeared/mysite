from calendar import c
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import UserCreationForm
import sweetify




# # login view function
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                # Extract username and password from the form
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                email = form.cleaned_data.get('email')

                # Check if email is provided, if so, set username to email
                if email:
                    username = email

                # Authenticate the user
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    # Login the user
                    login(request, user)
                    sweetify.success(request, 'Login successful!', persistent = 'ok')
                    return redirect('/')
            else:
                sweetify.error(request, 'Login failed. Please check your username and password.', persistent=':(')
                return redirect('/')  # Redirect back to the login page
        else:
            form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')




# logout view function
@login_required
def logout_view(request):
    logout(request)
    sweetify.success(request, 'Logout successful!')
    return redirect('/')






# signup view function
def signup_view(request):
   if not request.user.is_authenticated:
       if request.method == 'POST':
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               sweetify.success(request, 'signup successful')
               return redirect('/')
       form = UserCreationForm()
       context = {'form': form}
       return render(request, 'accounts/signup.html',context)
   else:
       return redirect('/')