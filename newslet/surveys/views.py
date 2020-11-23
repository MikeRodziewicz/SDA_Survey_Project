from django import views
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProductForm, CompanyForm, SurveyForm
from .models import Product, Company


class CompanyCreateView(LoginRequiredMixin, views.generic.CreateView):
    form_class = CompanyForm
    template_name = 'form.html'
    success_url = reverse_lazy('website-home')


class CompanyListView(LoginRequiredMixin, views.generic.ListView):
    template_name = 'company/companies.html'
    model = Company


class ProductCreateView(LoginRequiredMixin, views.generic.CreateView):
    form_class = ProductForm
    template_name = 'form.html'
    success_url = reverse_lazy('website-home')


class ProductListView(LoginRequiredMixin, views.generic.ListView):
    template_name = 'products/products_list.html'
    model = Product


class SurveyCreateView(LoginRequiredMixin, views.generic.CreateView):
    form_class = SurveyForm
    template_name = 'form.html'
    success_url = reverse_lazy('website-home')
