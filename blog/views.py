from unicodedata import category
from django.shortcuts import render, get_object_or_404
from blog.models import post 
from django.utils import timezone 



def blog_view(request):
    current_time = timezone.now()
    # using lte method to filter less than equal
    posts = post.objects.filter(status = 1, published_date__lte = current_time)
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)   




def blog_single(request, pid):
    # calculating the current time
    current_time = timezone.now()
    # set query to get all of the posts from the database
    all_posts = post.objects.filter(status = 1, published_date__lte = current_time)
    # set the default id for the post the user is requesting to watch that 
    current_index = 0

    # catch the order of the post that user is requesting to watch , it means that we are going to underestate that the post where putted
    for i , p in enumerate(all_posts):
        if p.id == pid:
            current_index = i
            break

    # making the prev and next posts
    prev_post = all_posts[current_index - 1] if current_index - 1 >= 0 else None 
    next_post = all_posts[current_index + 1] if current_index + 1 < len(all_posts) else None

    # getting specific post from the database by using the get object or 404 method 
    current_post = get_object_or_404(all_posts, pk = pid)
    # having auto increment about our post count of views 
    current_post.counted_view += 1
    current_post.save() 
    # insert information into the context and show them to the user
    context = {'Post' : current_post, 'prev_post' : prev_post , 'next_post' : next_post}
    return render(request , 'blog/blog-single.html', context)  




def  test(request):
    return render(request, 'test.html',)



def blog_category(request,cat_name):
    now = timezone.now()
    posts = post.objects.filter(status = True , published_date__lte=now)
    posts = posts.filter(category__name = cat_name)
    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)   