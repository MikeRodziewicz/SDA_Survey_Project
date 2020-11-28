from django import views
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProductForm, CompanyForm, SurveyForm
from .models import Product, Company
from website.mixins import TitleMixin

from django.shortcuts import render
from .random_users import random_users_emails_list


def winners(request):
    return render(
        request, template_name='random_users.html',
        context={'winners': random_users_emails_list()}
    )


class CompanyCreateView(LoginRequiredMixin, TitleMixin, views.generic.CreateView):
    title = 'Add Company'
    form_class = CompanyForm
    template_name = 'form.html'
    success_url = reverse_lazy('website-home')


class CompanyListView(LoginRequiredMixin, TitleMixin, views.generic.ListView):
    title = 'Companies'
    template_name = 'company/companies.html'
    model = Company


class ProductCreateView(LoginRequiredMixin, TitleMixin, views.generic.CreateView):
    title = 'Add Product'
    form_class = ProductForm
    template_name = 'form.html'
    success_url = reverse_lazy('website-home')


class ProductListView(LoginRequiredMixin, TitleMixin, views.generic.ListView):
    title = 'Products'
    template_name = 'products/products_list.html'
    model = Product


class SurveyCreateView(LoginRequiredMixin, TitleMixin, views.generic.CreateView):
    title = 'Add Survey'
    form_class = SurveyForm
    template_name = 'form.html'
    success_url = reverse_lazy('website-home')
