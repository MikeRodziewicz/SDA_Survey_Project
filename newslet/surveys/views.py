from django.shortcuts import render
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
from .models import Product, Company, Survey
from .random_users import random_users_emails_list


def winners(request):
    template_name = render_to_string('surveys/winners.html')
    winners = GuestSurvey.objects.all().order_by("?").values_list('quest_email', flat=True).first()

    email = EmailMessage(
    'Contratulations You Won!',
    template_name,
    settings.EMAIL_HOST_USER,
    bcc=[winners],
    )
    email.content_subtype = 'html'
    email.fail_silently=False
    email.send()

    messages.success(request,f'The winner is {winners}!')
    return render(request, 'surveys/winners_promo.html', context={'winners':winners})


def send_surveys(request, pk):
    template = render_to_string('website/survery_invitation.html',{'pk':pk})
    receipients = GuestSurvey.objects.all().values_list('quest_email', flat=True)
    email = EmailMessage(
    'please take the survey',
    template,
    settings.EMAIL_HOST_USER,
    bcc=receipients,
    )
    email.content_subtype = 'html'
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
            'survey_product_id': Survey.objects.all().values_list('product_id', flat=True)
        }
    paginate_by = 4
    
    def get_queryset(self):
        return Product.objects.filter(company=self.request.user.profile.user_company)


class ProductCreateView(LoginRequiredMixin, TitleMixin, views.generic.CreateView):
    title = 'Add Product'
    form_class = ProductForm
    template_name = 'surveys/form.html'
    success_url = reverse_lazy('manage_company')


class ProductUpdate(LoginRequiredMixin, TitleMixin, views.generic.UpdateView):
    title = 'Update Product'
    form_class = ProductForm
    template_name = 'surveys/form.html'
    model = Product
    success_url = reverse_lazy('manage_company')


class ProductDelete(LoginRequiredMixin, TitleMixin, views.generic.DeleteView):
    template = 'surveys/product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('manage_company')

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

    def get_queryset(self):
        return Product.objects.filter(company=self.request.user.profile.user_company)


class SurveyCreateView(LoginRequiredMixin, TitleMixin, views.generic.CreateView):
    form_class = SurveyForm
    template_name = 'surveys/survey_form.html'
    success_url = reverse_lazy('website-home')
    image = None

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_title(self):
        pk = self.kwargs['pk']
        title = escape(Product.objects.filter(id=pk).values('name')[0]['name'])
        return SafeString(title.capitalize())

    def get_image(self):
        pk = self.kwargs['pk']
        image = Product.objects.filter(id=pk).values('product_logo')[0]['product_logo']
        return image

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        image = self.get_image()
        if image is not None:
            result['image'] = image
        return result