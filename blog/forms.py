from .models import Blogpost

from django import forms 

class Blogspostform(forms.ModelForm):
    
    class Meta():
        model = Blogpost
        fields = ['title','description']
        