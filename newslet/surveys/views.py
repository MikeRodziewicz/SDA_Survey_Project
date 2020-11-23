from django.shortcuts import render
from website.models import GuestSurvey
from django.contrib.auth.decorators import login_required



def survey(request):
    return render(request, 'survey/survey.html')
