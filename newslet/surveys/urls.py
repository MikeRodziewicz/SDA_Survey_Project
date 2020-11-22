from django.urls import path
from . import views
from .views import ProductCreateView, ProductListView, CompanyCreateView, SurveyCreateView

urlpatterns = [
    path('surveys/add_product', ProductCreateView.as_view(), name='product_create'),
    path('surveys/list', ProductListView.as_view(), name='products_list'),
    path('surveys/add_company', CompanyCreateView.as_view(), name='company_create'),
    path('surveys/add_survey', SurveyCreateView.as_view(), name='survey_create')

]
