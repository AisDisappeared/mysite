from multiprocessing import context
from django.shortcuts import render
from blog.models import post

def blog_view(request):
    return render(request , 'blog/blog-home.html')                     

def blog_single(request):
    return render(request , 'blog/blog-single.html')  

def test(request):
    rows = post.objects.all()
    context = {'posts' : rows }
    return render(request , 'test.html' , context)



