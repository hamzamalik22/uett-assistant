from django import forms
from django.forms import ModelForm
from uettApp.models import *
from .models import * 

class DepForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class SemForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = '__all__'

class SubForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'