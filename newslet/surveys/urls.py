from django.urls import path
from . import views

urlpatterns = [
    path('surveys', views.survey, name='surveys-home'),

]
