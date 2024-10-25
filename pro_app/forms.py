from django import forms
from .models import Commant

class Commant_Form(forms.ModelForm):
    class Meta:
        model = Commant
        fields = ['email','your_comment']
        widgets = {

            
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'your_comment': forms.TextInput(attrs={'class': 'form-control'}),
        }

