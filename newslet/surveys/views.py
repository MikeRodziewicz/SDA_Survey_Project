from django import views
from django.urls import reverse_lazy

from .forms import ProductForm, CompanyForm, SurveyForm
from .models import Product


class CompanyCreateView(views.generic.CreateView):
    form_class = CompanyForm
    template_name = 'form.html'
    success_url = reverse_lazy('website-home')


class ProductCreateView(views.generic.CreateView):
    form_class = ProductForm
    template_name = 'form.html'
    success_url = reverse_lazy('website-home')


class ProductListView(views.generic.ListView):
    template_name = 'products/products_list.html'
    model = Product


class SurveyCreateView(views.generic.CreateView):
    form_class = SurveyForm
    template_name = 'form.html'
    success_url = reverse_lazy('website-home')
