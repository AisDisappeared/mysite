from django import template
from blog.models import post 
from django.utils import timezone

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
    posts = post.objects.filter(status = True).order_by('published_date')[:4]
    return {'posts' : posts}