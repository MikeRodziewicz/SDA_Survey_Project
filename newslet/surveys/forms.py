from django import forms

import re
import math

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML

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
            'product_logo',
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
    class Meta:
        model = Survey
        fields = ('rate_1', 'rate_2', 'rate_3', 'rate_4', 'rate_5', 'description')

        