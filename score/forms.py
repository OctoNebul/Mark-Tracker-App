from django import forms
from score.models import Score # in score app => models.py => Score class

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['name', 'value'] 
