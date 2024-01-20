from django.shortcuts import render,get_object_or_404
from blog.models import post
from django.utils import timezone 
from django.db.models import F 



def blog_view(request):
    current_time = timezone.now()
    # using lte method to filter less than equal
    posts = post.objects.filter(published_date__lte=current_time,status=1)
    context = {'posts' : posts }
    return render(request , 'blog/blog-home.html' , context)                     

def blog_single(request,pid):
    current_time = timezone.now()
    posts = post.objects.filter(published_date__lte=current_time,status=1)
    # we use F function to have auto increment for counted posts views
    posts.update(counted_view=F('counted_view')+1)
    posts = get_object_or_404(posts,pk=pid)
    context = {'post':posts}
    return render(request , 'blog/blog-single.html',context)  

