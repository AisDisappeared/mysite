from django.db import models
from django.forms import EmailField



# contact table
class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    uptated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return '{} - {}'.format(self.name, self.id)
    


# Newsletter table 
class Newsletter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email 