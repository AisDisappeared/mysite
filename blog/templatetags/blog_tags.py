from django import template
from blog.models import post 
from django.utils import timezone

register = template.Library()

@register.simple_tag
def posts_numbs():
    now = timezone.now()
    count_of_posts = post.objects.filter(status = True , published_date__lte=now).count()
    return count_of_posts 


@register.filter
def truncate(content,arg=20):
    return content[:arg]