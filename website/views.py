import re
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse 
from website.models import contact 
from website.forms import Nameform

def index_view(request):
    return render (request , 'website/index.html')

def contact_view(request):
    return render (request , 'website/contact.html')

def about_view(request):
    return render (request , 'website/about.html')                      

def test(request):
    if request.method == 'POST':
        form_data_posted = Nameform(request.POST)
        if form_data_posted.is_valid():
            name = form_data_posted.cleaned_data['name']
            email = form_data_posted.cleaned_data['email']
            subject = form_data_posted.cleaned_data['subject']
            message = form_data_posted.cleaned_data['message']
            
            return HttpResponse('success')
        else:
            return HttpResponse('Not a valid form data')
         
    form = Nameform()
    return render (request , 'test.html' , {'form':form})
