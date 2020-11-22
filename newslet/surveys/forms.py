from django import forms

import re
import math

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

from .models import Product, Company, Survey


def truncate(number, digits):
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


class CompanyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            Submit('submit', 'Add Company', css_class="btn-success"),
            )

    class Meta:
        model = Company
        fields = '__all__'


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'price',
            Submit('submit', 'Add Product', css_class="btn-success"),
            )

    class Meta:
        model = Product
        fields = '__all__'

    def clean_price(self):
        initial = self.cleaned_data['price']
        cleaned = truncate(initial, 2)
        self.cleaned_data['price'] = cleaned
        return cleaned


class SurveyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'question',
            'answer',
            Submit('submit', 'Add Survey', css_class="btn-success"),
            )

    class Meta:
        model = Survey
        fields = '__all__'

    question = forms.CharField()
    answer = forms.CharField(widget=forms.Textarea, required=False)

    def clean_answer(self):
        initial = self.cleaned_data['answer']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        cleaned = '. '.join(sentence.capitalize() for sentence in sentences)
        self.cleaned_data['answer'] = cleaned
        return cleaned
