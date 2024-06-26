from django import forms 
from blog.models import Comment 
from captcha.fields import CaptchaField 



class Commentform(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['post','name', 'subject', 'message']