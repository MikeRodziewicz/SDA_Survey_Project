from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import NewsCategory, Formularz
from .forms import NewsCategoryForm, NewsTagsForm, FormularzForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView
)


def add_formularz(request):
    if request.method == 'POST':
        form = FormularzForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website-home')
    else:
        form = FormularzForm()
    return render(request, 'website/home.html', {'form':form})

def home(request):
    if request.method == 'POST':
        form = FormularzForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website-home')
    else:
        form = FormularzForm()
    return render(request, 'website/home.html', {'form':form})


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
    return render(request, 'website/create_category.html')



def add_tag(request):
    if request.method == 'POST':
        form = NewsTagsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website-home')
    else:
        form = NewsTagsForm()
    return render(request, 'website/create_tag.html')

class NewsCategoryDetailView(DetailView):
    model = NewsCategory
