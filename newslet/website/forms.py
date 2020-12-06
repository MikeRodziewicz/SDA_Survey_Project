from django import forms
from .models import GuestSurvey


class GuestSurveyForm(forms.ModelForm):
    class Meta:
        model = GuestSurvey
        fields = ['guest_name', 'quest_email']
        labels = {
            'guest_name':'Name',
            'quest_email':'Email'

        }

    widgets = {
        'guest_name': forms.TextInput(attrs={'class': 'form-control'}),
        'quest_email': forms.EmailInput(attrs={'class': 'form-control'})
    }

