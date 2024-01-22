from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.utils import timezone 



def blog_view(request):
    current_time = timezone.now()
    # using lte method to filter less than equal
    posts = post.objects.filter(published_date__lte=current_time,status=1)
    context = {'posts' : posts }
    return render(request , 'blog/blog-home.html' , context)                     

def blog_single(request,pid,):
    current_time = timezone.now()
    posts = post.objects.filter(published_date__lte=current_time,status=1)
    p = get_object_or_404(posts,pk=pid)
    p.counted_view += 1
    p.save()
    context = {'post':p}
    return render(request , 'blog/blog-single.html',context)  

