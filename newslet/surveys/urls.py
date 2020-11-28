from django.urls import path
from django.contrib.auth.views import LoginView

from .views import ProductCreateView, ProductListView, CompanyCreateView, CompanyListView, SurveyCreateView, winners

urlpatterns = [
    path('surveys/add_product', ProductCreateView.as_view(), name='product_create'),
    path('surveys/list', ProductListView.as_view(), name='products_list'),
    path('surveys/add_company', CompanyCreateView.as_view(), name='company_create'),
    path('surveys/companies', CompanyListView.as_view(), name='companies'),
    path('surveys/add_survey', SurveyCreateView.as_view(), name='survey_create'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('surveys/winners', winners, name='winners')
]
