from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime

def get_dummy_user():
    return {
        "name": "John Doe",
        "balance": 100005,
        "phone": "081234567890",
        "email": "john@doe.com",
        "address": "somewhere in the world",
        "transaction_date": datetime.now().strftime("%Y-%m-%d")
    }

# @login_required
def mypay_dashboard(request):
    user = get_dummy_user()
    transactions = [
        {'amount': 50000, 'date': '2023-10-01', 'description': 'Pembelian Pulsa'},
        {'amount': 20000, 'date': '2023-09-25', 'description': 'Pembelian Token Listrik'},
        {'amount': 30000, 'date': '2023-09-20', 'description': 'Pembelian Voucher Game'},
    ]

    context = {
        'user': user,
        'balance': user['balance'],
        'transactions': transactions
    }
    return render(request, 'mypay/dashboard.html', context)

# @login_required
def mypay_transaction(request):
    user = get_dummy_user()
    if request.method == 'POST':
        # Proses transaksi di sini
        return redirect('mypay_dashboard')
    
    context = {
        'user': user
    }
    return render(request, 'mypay/transaction.html', context)