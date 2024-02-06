from calendar import c
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
import sweetify

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            sweetify.success(request , 'login successful')
            return redirect('/')
    message = 'login failed'
    context = {'message': message}
    return render(request, 'accounts/login.html', context)

# def logout_view(request):
    # return  

def signup_view(request):
    return render(request,'accounts/signup.html')
