from dataclasses import fields
from django import forms 
from django.forms import ModelForm
from website.models import contact,Newsletter
from captcha.fields import CaptchaField 



# form method for working with forms
class Nameform(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea) 



# model form for making forms base on models 
class contactform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = contact 
        fields = '__all__' 



# model form for making forms base on models 
class NewsletterForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Newsletter
        fields = '__all__'
