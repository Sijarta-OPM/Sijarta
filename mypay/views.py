from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
import uuid

# Variabel global untuk menyimpan data dummy service orders
SERVICE_ORDERS = [
    {'id': 1, 'category': 'Home Cleaning', 'subcategory': 'Regular Cleaning', 'status': 'Mencari Pekerja Terdekat', 'alamat': 'Jl. Mangga Tiga No. 42', 'tanggal': '2024-05-11', 'waktu': '09:30', 'harga': 'Rp 150.000'},
    {'id': 2, 'category': 'Home Cleaning', 'subcategory': 'Deep Cleaning', 'status': 'Mencari Pekerja Terdekat', 'alamat': 'Jl. Mangga Dua No. 20', 'tanggal': '2024-05-21', 'waktu': '10:00', 'harga': 'Rp 200.000'},
    {'id': 3, 'category': 'Gardening', 'subcategory': 'Lawn Mowing', 'status': 'Mencari Pekerja Terdekat', 'alamat': 'Jl. Melati No. 5', 'tanggal': '2024-05-19', 'waktu': '08:00', 'harga': 'Rp 100.000'},
]

def get_dummy_user():
    return {
        "id": uuid.uuid4(),
        "name": "John Doe",
        "balance": 100005,
        "phone": "081234567890",
        "email": "john@doe.com",
        "address": "somewhere in the world",
        "transaction_date": datetime.now().strftime("%Y-%m-%d")
    }

def get_dummy_worker():
    return {
        "id": uuid.uuid4(),
        "name": "Jane Doe",
        "password": "password123",
        "jenis_kelamin": "Perempuan",
        "no_hp": "081234567891",
        "tanggal_lahir": "1990-01-01",
        "alamat": "somewhere else in the world",
        "nama_bank": "Bank ABC",
        "nomor_rekening": "1234567890",
        "npwp": "123456789012345",
        "link_foto": "http://example.com/photo.jpg"
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

# @login_required
def service_orders(request):
    user = get_dummy_user()
    
    global SERVICE_ORDERS

    selected_category = request.GET.get('category')
    selected_subcategory = request.GET.get('subcategory')

    filtered_orders = [order for order in SERVICE_ORDERS if order['status'] == 'Mencari Pekerja Terdekat']

    if selected_category:
        filtered_orders = [order for order in filtered_orders if order['category'] == selected_category]
        if selected_subcategory:
            filtered_orders = [order for order in filtered_orders if order['subcategory'] == selected_subcategory]

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        for order in SERVICE_ORDERS:
            if order['id'] == int(order_id):
                order['status'] = 'Menunggu Pekerja Terdekat'
                break
        return redirect('service_orders')

    context = {
        'user': user,
        'service_orders': filtered_orders,
        'categories': list(set(order['category'] for order in SERVICE_ORDERS)),
        'subcategories': list(set(order['subcategory'] for order in SERVICE_ORDERS if order['category'] == selected_category)) if selected_category else []
    }
    return render(request, 'mypay/service_orders.html', context)