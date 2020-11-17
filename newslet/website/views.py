from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import NewsCategory
from .forms import NewsCategoryForm, NewsTagsForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html', {'category':NewsCategory.objects.all()})



def add_category(request):
    if request.method == 'POST':
        form = NewsCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website-home')
    else:
        form = NewsCategoryForm()
    return render(request, 'website/create_category.html', {'form':form})



def add_tag(request):
    if request.method == 'POST':
        form = NewsTagsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website-home')
    else:
        form = NewsTagsForm()
    return render(request, 'website/create_tag.html', {'form':form})
