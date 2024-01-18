from multiprocessing import context
from telnetlib import STATUS
from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.utils import timezone 
from django.db.models import F 



def blog_view(request):
    post.objects.filter(status=True).update(counted_view=F('counted_view')+1)
    current_time = timezone.now()
    rows = post.objects.filter(published_date__lte=current_time,status=1)
    context = {'posts' : rows }
    return render(request , 'blog/blog-home.html' , context)                     

def blog_single(request):
    return render(request , 'blog/blog-single.html')  

def test(request ,pid):
    posts = get_object_or_404(post,pk=pid)
    context = {'post':posts}
    return render(request , 'test.html' , context)


