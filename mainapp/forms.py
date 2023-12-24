from django import forms
from .models import Message
from django.contrib.auth.forms import UserCreationForm

class Messageform(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['full_name','phone_number','email','message']
        
    def __init__(self,*args,**kvargs):
        super(Messageform,self).__init__(*args,**kvargs)
