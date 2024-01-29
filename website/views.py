import re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse 
from website.models import contact 
from website.forms import Nameform ,contactform ,NewsletterForm 


# home page
def index_view(request):
    return render (request , 'website/index.html')


# contact page
def contact_view(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
    form = contactform(request.POST)
    return render (request , 'website/contact.html',{'form':form})



# about page
def about_view(request):
    return render (request , 'website/about.html')                      




def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')



# test part 
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
