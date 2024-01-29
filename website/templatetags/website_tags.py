from django import template 
from django.utils import timezone 
from blog.models import post 


register = template.Library()


@register.inclusion_tag('website/Sixlatest.html')
def sixlatest():
   now = timezone.now()
   posts = post.objects.filter(status = True ,published_date__lte=now).order_by('-published_date')[:6]
   return {'posts': posts}
