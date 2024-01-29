from django import template 
from django.utils import timezone 
from blog.models import post 


register = template.Library()


@register.inclusion_tag('website/Sixlatest.html')
def sixlatest():
   posts = post.objects.filter(status = True).order_by('-published_date')[:6]
   return {'posts': posts}