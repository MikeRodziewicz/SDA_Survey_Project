from django import forms
from django.forms import CharField
from .models import NewsCategory, NewsTags

class NewsTagsForm(forms.ModelForm):
    tag_name = forms.CharField()

    class Meta:
        model = NewsTags
        fields = ['tag_name']

class NewsCategoryForm(forms.ModelForm):
    category_name  = forms.CharField()

    class Meta:
        model = NewsCategory
        fields = ['category_one', 'assigned_tag']
