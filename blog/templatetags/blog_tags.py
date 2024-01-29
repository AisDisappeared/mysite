from unicodedata import category
from django import template
from blog.models import post 
from django.utils import timezone
from blog.models import Category 

register = template.Library()
# simple tag
@register.simple_tag(name='totalposts')
def posts_numbs():
    now = timezone.now()
    count_of_posts = post.objects.filter(status = True , published_date__lte=now).count()
    return count_of_posts 

# simple tag
@register.simple_tag(name='posts')
def all_posts():
    now = timezone.now()
    posts = post.objects.all()
    return posts

# filter tag
@register.filter
def snippet(content,arg=20):
    return content[:arg]


# inclusion tag 
@register.inclusion_tag('blog/blog-popularposts.html')
def latestposts():
    posts = post.objects.filter(status = True).order_by('-published_date')[:4]
    return {'posts' : posts}


# inclusion tag 
@register.inclusion_tag('blog/blog-post-categories.html') 
def postCats():
    now = timezone.now()
    posts = post.objects.filter(status = True ,published_date__lt=now)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        c = posts.filter(category=name).count()
        cat_dict[name] = c 
    return {'categories' : cat_dict}
             
         
