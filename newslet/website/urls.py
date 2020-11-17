from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('add_category',views.add_category, name='add_category'),
    path('add_tag',views.add_tag, name='add_tag')
]
