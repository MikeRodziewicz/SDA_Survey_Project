from django.shortcuts import render
from website.models import GuestSurvey
from django.contrib.auth.decorators import login_required
from django import views
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import ProductForm, CompanyForm, SurveyForm
from .models import Product, Company
from website.mixins import TitleMixin

from django.shortcuts import render
from .random_users import random_users_emails_list
from django.views.generic import CreateView


def winners(request):
    return render(
        request, template_name='surveys/random_users.html',
        context={'winners': random_users_emails_list()}
    )


class CompanyCreateView(LoginRequiredMixin, TitleMixin, views.generic.CreateView):
    title = 'Add Company'
    form_class = CompanyForm
    template_name = 'surveys/form.html'
    success_url = reverse_lazy('website-home')


class CompanyListView(LoginRequiredMixin, TitleMixin, views.generic.ListView):
    title = 'Companies'
    template_name = 'surveys/companies.html'
    model = Company


class ProductCreateView(LoginRequiredMixin, TitleMixin, views.generic.CreateView):
    title = 'Add Product'
    form_class = ProductForm
    template_name = 'surveys/form.html'
    success_url = reverse_lazy('website-home')


class ProductUpdate(LoginRequiredMixin, TitleMixin, views.generic.UpdateView):
    title = 'Update Product'
    form_class = ProductForm
    template_name = 'surveys/form.html'
    model = Product
    success_url = reverse_lazy('website-home')


class ProductListView(LoginRequiredMixin, TitleMixin, views.generic.ListView):
    title = 'Products'
    template_name = 'surveys/products_list.html'
    model = Product


class SurveyCreateView(LoginRequiredMixin, TitleMixin, views.generic.CreateView):
    title = 'Add Survey'
    form_class = SurveyForm
    template_name = 'surveys/form.html'
    success_url = reverse_lazy('website-home')
