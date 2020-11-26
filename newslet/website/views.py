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


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


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


def send_surveys(request):
    template = render_to_string('website/survery_invitation.html')
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
