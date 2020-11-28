from django import forms
from .models import GuestSurvey


class GuestSurveyForm(forms.ModelForm):
    class Meta:
        model = GuestSurvey
        fields = ['guest_name', 'quest_email']

