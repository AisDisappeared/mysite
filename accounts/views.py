from django.shortcuts import render

def login_view(request):
    return render(request, 'accoutn/login.html')

# def logout_view(request):
    # return  

def signup_view(request):
    return render(request,'accounts/signup.html')