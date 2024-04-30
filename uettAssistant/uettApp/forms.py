# forms.py
from django import forms
from .models import *

class GradeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        subjects = kwargs.pop('subjects')
        super(GradeForm, self).__init__(*args, **kwargs)
        for subject in subjects:
            choices = [('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'),
                       ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D', 'D'), ('F', 'F')]
            self.fields[f'grade_{subject.id}'] = forms.ChoiceField(
                choices=choices,
                label=subject.name,
                widget=forms.Select(attrs={'class': 'form-select'})
            )