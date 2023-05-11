from django import forms
from .models import Input_Images

class Input_ImagesForm(forms.ModelForm):
    
    class Meta:
        model = Input_Images
        fields = ["image"]


