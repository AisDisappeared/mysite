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
    current_post = get_object_or_404(posts,pk=pid)
    related_posts = post.objects.filter(category__in = current_post.category.all())
    # auto increment for counting views whenever a post is opened
    current_post.counted_view += 1
    current_post.save()
    context = {'post':current_post , 
               'prev': related_posts.filter(id__lt=current_post.id).order_by('-id').first(), 'next': 
               related_posts.filter(id__gt=current_post.id).order_by('-id').first()}
    return render(request , 'blog/blog-single.html',context)  

