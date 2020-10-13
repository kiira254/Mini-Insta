from django import forms
from .models import Image

class LetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class ImageForm(forms.ModelForm):
    model = Image
    exclude = ['editor']
    widgets = {
        'likes': forms.CheckboxSelectMultiple() 
    }