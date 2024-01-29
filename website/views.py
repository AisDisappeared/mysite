import re
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse 
from website.models import contact 
from website.forms import Nameform ,contactform

def index_view(request):
    return render (request , 'website/index.html')

def contact_view(request):
    return render (request , 'website/contact.html')

def about_view(request):
    return render (request , 'website/about.html')                      

def test(request):
    if request.method == 'POST':
        form_data_posted = contactform(request.POST)
        if form_data_posted.is_valid():
            form_data_posted.save()
            return HttpResponse('success')
        else:
            return HttpResponse('Not a valid form data')
         
    form = contactform()
    return render (request , 'test.html' , {'form':form})
