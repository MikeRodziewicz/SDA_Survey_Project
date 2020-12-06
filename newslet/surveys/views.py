from django.shortcuts import render
from website.models import GuestSurvey
from django.contrib.auth.decorators import login_required
from django import views
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.html import escape
from django.utils.safestring import SafeString

from website.mixins import TitleMixin

from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from website.forms import  GuestSurveyForm
from website.models import GuestSurvey


from .forms import ProductForm, CompanyForm, SurveyForm
from .models import Product, Company
from .random_users import random_users_emails_list


def winners(request):
    return render(
        request, template_name='surveys/random_users.html',
        context={'winners': random_users_emails_list()}
    )


def send_surveys(request, pk):
    template = render_to_string('website/survery_invitation.html',{'pk':pk})
    receipients = GuestSurvey.objects.all().values_list('quest_email', flat=True)
    email = EmailMessage(
    'please take the survey',
    template,
    settings.EMAIL_HOST_USER,
    bcc=receipients,
    )
    email.fail_silently=False
    email.send()

    messages.success(request,f'Surveys Sent!')
    return render(request, 'website/send_surveys.html')


class ManageCompany(views.generic.ListView):
    template_name = 'surveys/manage_company.html'
    model = Product
    extra_context = {
            'products': Product.objects.all(),
            'survey_users': GuestSurvey.objects.all().count(),
        }


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


class ProductDelete(LoginRequiredMixin, TitleMixin, views.generic.DeleteView):
    template = 'surveys/product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('products_list')

    def get_title(self):
        safe_title = escape(self.object.name)
        return SafeString(f'Delete <em>{safe_title}</em>')


class ProductDetail(LoginRequiredMixin, TitleMixin, views.generic.DetailView):
    template = 'surveys/product_detail.html'
    model = Product

    def get_title(self):
        return self.object.name


class ProductListView(LoginRequiredMixin, TitleMixin, views.generic.ListView):
    title = 'Products'
    template_name = 'surveys/products_list.html'
    model = Product


class SurveyCreateView(LoginRequiredMixin, TitleMixin, views.generic.CreateView):
    title = 'Add Survey'
    form_class = SurveyForm
    template_name = 'surveys/form.html'

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)
    
    success_url = reverse_lazy('website-home')


