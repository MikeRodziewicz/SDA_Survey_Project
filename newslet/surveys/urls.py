from django.urls import path

from .views import ProductCreateView, ProductListView,\
    SurveyCreateView, winners, ProductUpdate, ProductDelete, ProductDetail, ManageCompany

from .views import send_surveys
from surveys import views

urlpatterns = [
    path('surveys/add_product/', ProductCreateView.as_view(), name='product_create'),
    path('surveys/manage_company/', ManageCompany.as_view(), name='manage_company'),
    path('surveys/list', ProductListView.as_view(), name='products_list'),
    path('surveys/update/<int:pk>', ProductUpdate.as_view(), name='update_product'),
    path('surveys/delete/<int:pk>', ProductDelete.as_view(), name='delete_product'),
    path('surveys/detail/<int:pk>', ProductDetail.as_view(), name='detail_product'),
    path('send_surveys/<int:pk>', send_surveys, name='send_surveys'),
    path('surveys/add_survey/<int:pk>', SurveyCreateView.as_view(), name='survey_create'),
    path('surveys/winners', winners, name='winners'),
    path('surveys/send_surveys/<int:pk>', views.send_surveys, name='send_surveys')
]
