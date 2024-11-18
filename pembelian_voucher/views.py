from django.shortcuts import render
from mypay.views import *


def get_beli_voucher_form(request):
    user = get_dummy_user()
    
    context = {
        'user': user,
    }
    return render(request, 'beli_voucher.html')