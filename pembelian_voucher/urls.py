from django.urls import path
from .views import get_beli_voucher_form

app_name = 'review'

urlpatterns = [
    path('beli_voucher/', get_beli_voucher_form, name='beli_voucher'),
]