from django.shortcuts import render, redirect
from .forms import UserRegister


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data('username')
            return redirect('home')
    else:
        form = UserRegister()
    return render(request, 'users/register.html', {form:'form'})
