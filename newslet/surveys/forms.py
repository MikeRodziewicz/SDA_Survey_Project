from django import forms

import re
import math

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Row

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
            'company',
            'name',
            'price',
            'product_logo',
            Row(
                Submit('submit', 'Save Item', css_class="btn-success"),
                HTML("""<a class="btn btn-danger" type="button" href="{% url 'manage_company' %}">Cancel</a>""")
            )
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
        self.fields['rate_1'].label = 'Jak oceniasz jakosc produktu?'
        self.fields['rate_2'].label = 'Jak oceniasz cene produktu?'
        self.fields['rate_3'].label = 'Ocen jaka wartosc ma dla Ciebie produkt?'
        self.fields['rate_4'].label = 'Jak oceniasz nasza firme?'
        self.fields['rate_5'].label = 'Jak oceniasz kontakt z klientem?'
        self.fields['description'].label = 'Napisz nam coś o produkcie:'
        self.helper.layout = Layout(
            'rate_1',
            'rate_2',
            'rate_3',
            'rate_4',
            'rate_5',
            'description',
            Row(
                Submit('submit', 'Add Survey', css_class="btn-success"),
                HTML("""<a class="btn btn-danger" type="button" href="{% url 'manage_company' %}">Cancel</a>""")
            )
        )

    class Meta:
        model = Survey
        fields = '__all__'

    rate_1 = forms.IntegerField(min_value=1, max_value=5)
    rate_2 = forms.IntegerField(min_value=1, max_value=5)
    rate_3 = forms.IntegerField(min_value=1, max_value=5)
    rate_4 = forms.IntegerField(min_value=1, max_value=5)
    rate_5 = forms.IntegerField(min_value=1, max_value=5)
    description = forms.CharField(widget=forms.Textarea, required=False)

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        cleaned = '. '.join(sentence.capitalize() for sentence in sentences)
        self.cleaned_data['description'] = cleaned
        return cleaned