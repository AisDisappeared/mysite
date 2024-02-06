from calendar import c
from django.shortcuts import render

def login_view(request):
    if request.user.is_authenticated:
        message = f'Login successful as {request.user.username}'
        context = {'message': message}
    else:
        message = f'Login not successful as {request.user.username}'
        context = {'message': message}    
    return render(request, 'accounts/login.html', context)

# def logout_view(request):
    # return  

def signup_view(request):
    return render(request,'accounts/signup.html')
