from calendar import c
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import sweetify


# login view function
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request , data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                # email = form.cleaned_data['email']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    sweetify.success(request , 'login successful')
                    return redirect('/')
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')



# logout view function
@login_required
def logout_view(request):
    logout(request)
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