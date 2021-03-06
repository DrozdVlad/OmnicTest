from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/token', obtain_auth_token, name='token'),
    path('currencys/', views.CurrencyListView.as_view(), name='currencys')
]
