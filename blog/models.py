import email
from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField, EmailField
from django.urls import reverse
from taggit.managers import TaggableManager




class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name 



class post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    tags = TaggableManager()
    category = models.ManyToManyField(Category) 
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_required = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
 
    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})
    

class Comment(models.Model):
    post = models.ForeignKey(post , on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)  
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length = 255)
    message = models.TextField() 
    approved = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name 
    
    
    class Meta:
        ordering = ['-created_date']