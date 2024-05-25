from django import forms
from .models import *

class TitlePageForm(forms.ModelForm):
    class Meta:
        model = TitlePage
        fields = ['department', 'title', 'topic', 'instructor', 'course', 'reg_no', 'name' , 'date', 'section']
