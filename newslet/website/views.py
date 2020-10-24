from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {
        'name': "mike"
    }
    return render(request, 'website/home.html', context)
