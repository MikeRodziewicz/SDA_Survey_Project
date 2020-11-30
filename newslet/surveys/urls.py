from django.urls import path

from .views import ProductCreateView, ProductListView, CompanyCreateView, CompanyListView,\
    SurveyCreateView, winners, ProductUpdate

from website.views import send_surveys

urlpatterns = [
    path('surveys/add_product', ProductCreateView.as_view(), name='product_create'),
    path('surveys/list', ProductListView.as_view(), name='products_list'),
    path('surveys/update/<int:pk>', ProductUpdate.as_view(), name='update_product'),
    path('surveys/add_company', CompanyCreateView.as_view(), name='company_create'),
    path('surveys/companies', CompanyListView.as_view(), name='companies'),
    path('surveys/add_survey', SurveyCreateView.as_view(), name='survey_create'),
    path('send_surveys/<int:pk>', send_surveys, name='send_surveys'),
    path('surveys/winners', winners, name='winners')
]
