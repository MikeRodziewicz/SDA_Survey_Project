from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegister, UserProfileUpdateForm, UserUpdateForm, CompanyRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        form_1 = CompanyRegisterForm(request.POST)
        if form.is_valid() and form_1.is_valid():
            username = form.cleaned_data.get('username')
            company = form_1.save()
            user = form.save()
            user.profile.user_company = company
            user.save()
            return redirect('website-home')
    else:
        form = UserRegister()
        form_1 = CompanyRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'form_1':form_1})



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST,
                                        request.FILES,
                                        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('website-home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html',context)
