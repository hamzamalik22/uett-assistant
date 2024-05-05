from django import forms
from .models import *

class TitlePageForm(forms.ModelForm):
    class Meta:
        model = TitlePage
        fields = ['title', 'instructor', 'course', 'reg_no', 'user' , 'date']
