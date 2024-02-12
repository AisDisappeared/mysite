from django import forms 
from django.contrib.auth.models import User 



class RegisterForm(forms.ModelForm):
    email = forms.EmailField()
    

    class Meta:
        model = User 
        fields = ['email' , 'username']



class Loginform(forms.Form):
    email = forms.EmailField()
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.Textarea)