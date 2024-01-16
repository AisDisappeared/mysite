from django.db import models

# Create your models here.
class post(models.Model):
    # image
    # tag
    # category
    # author
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return '{} - {}'.format(self.title , self.id)