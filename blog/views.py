from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from blog.models import post

def blog_view(request):
    rows = post.objects.filter(status = 1)
    context = {'posts' : rows }
    return render(request , 'blog/blog-home.html' , context)                     

def blog_single(request):
    return render(request , 'blog/blog-single.html')  

def test(request ,pid):
    posts = get_object_or_404(post,pk=pid)
    context = {'post':posts}
    return render(request , 'test.html' , context)


