from django import forms
from django.forms import CharField
from .models import NewsCategory, NewsTags, Formularz
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class FormularzForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'imie',
            'email',
            Submit('submit', 'Add product', css_class="btn-success"),
            )

    class Meta:
        model = Formularz
        fields = ['imie', 'email']

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
