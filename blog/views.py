from multiprocessing import context
from django.shortcuts import render
from blog.models import post

def blog_view(request):
    rows = post.objects.filter(status = 1)
    context = {'posts' : rows }
    return render(request , 'blog/blog-home.html' , context)                     

def blog_single(request):
    return render(request , 'blog/blog-single.html')  

def test(request):
    rows = post.object.all()
    context = {'posts' : rows}
    return render(request , 'test.html' , context)



