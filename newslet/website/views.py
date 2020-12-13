from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import  GuestSurveyForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from website.models import GuestSurvey
from surveys.models import Product
from .stats import survey_users_all, products_all, surveys_taken_all
from surveys.templatetags.surveys_extra import *
from surveys.templatetags.surveys_extra import product_averages



def home(request):
    if request.user.is_anonymous:  
        return render(request, 'website/home.html')
    company_products = Product.objects.filter(company=request.user.profile.user_company)
    max_avg, min_avg = product_averages(company_products)
    context = {
        'survey_users_all':survey_users_all,
        'products_all':products_all,
        'surveys_taken_all':surveys_taken_all,
        'products': company_products,
        'survey_product_id': Survey.objects.all().values_list('product_id', flat=True),
        'survey_users': Survey.objects.all().count(),
        'max_avg': max_avg,
        'min_avg': min_avg
    }
    return render(request, 'website/home.html', context)
     


def sign_up(request):
    if request.method == 'POST':
        form = GuestSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('survey_thanks')
    else:
        form = GuestSurveyForm()
    return render(request, 'website/survey_sign_up.html', {'form':form})

def survey_thanks(request):
    return render(request, 'website/survey_thanks.html')



