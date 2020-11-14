from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')
