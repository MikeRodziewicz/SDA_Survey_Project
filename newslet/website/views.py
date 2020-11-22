from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import  GuestSurveyForm
from django.contrib.auth.decorators import login_required


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
