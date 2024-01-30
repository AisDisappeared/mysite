from unicodedata import category
from django.shortcuts import render, get_object_or_404
from blog.models import post 
from django.utils import timezone 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# blog home view 
def blog_view(request,cat_name=None,author_username=None):
    current_time = timezone.now()
    # using lte method to filter less than equal
    posts = post.objects.filter(status = True, published_date__lte = current_time)
    if cat_name:
         posts = posts.filter(category__name = cat_name)
    if author_username:
        posts = posts.filter(author__username= author_username)

    p = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = p.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)   




# blog single view
def blog_single(request, pid):
    current_time = timezone.now()
    all_posts = post.objects.filter(status = 1, published_date__lte = current_time)
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
    current_post.counted_view += 1
    current_post.save() 
    context = {'Post' : current_post, 'prev_post' : prev_post , 'next_post' : next_post}
    return render(request , 'blog/blog-single.html', context)  





# search view 
def blog_search(request):
    now = timezone.now()
    posts = post.objects.filter(status = 1 , published_date__lte=now)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts' : posts}
    return render(request , 'blog/blog-home.html' , context)   












