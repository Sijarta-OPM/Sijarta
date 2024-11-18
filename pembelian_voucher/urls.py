from django.urls import path
from .views import beli_voucher

app_name = 'review'

urlpatterns = [
    path('beli_voucher/', beli_voucher, name='beli_voucher'),
]