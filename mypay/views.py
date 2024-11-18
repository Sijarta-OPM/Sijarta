from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
import uuid

def get_dummy_job_orders():
    return [
        {'id': 1, 'category': 'Home Cleaning', 'subcategory': 'Regular Cleaning', 'status': 'Menunggu Pekerja Berangkat', 'alamat': 'Jl. Mangga Tiga No. 42', 'tanggal': '2024-05-11', 'waktu': '09:30', 'harga': 'Rp 150.000'},
        {'id': 2, 'category': 'Home Cleaning', 'subcategory': 'Deep Cleaning', 'status': 'Pekerja Tiba Di Lokasi', 'alamat': 'Jl. Mangga Dua No. 20', 'tanggal': '2024-05-21', 'waktu': '10:00', 'harga': 'Rp 200.000'},
        {'id': 3, 'category': 'Gardening', 'subcategory': 'Lawn Mowing', 'status': 'Pelayanan Jasa Sedang Dilakukan', 'alamat': 'Jl. Melati No. 5', 'tanggal': '2024-05-19', 'waktu': '08:00', 'harga': 'Rp 100.000'},
        {'id': 4, 'category': 'Gardening', 'subcategory': 'Tree Trimming', 'status': 'Pesanan Selesai', 'alamat': 'Jl. Kenanga No. 10', 'tanggal': '2024-05-15', 'waktu': '14:00', 'harga': 'Rp 250.000'},
        {'id': 5, 'category': 'Home Cleaning', 'subcategory': 'Regular Cleaning', 'status': 'Menunggu Pekerja Berangkat', 'alamat': 'Jl. Anggrek No. 7', 'tanggal': '2024-05-18', 'waktu': '11:00', 'harga': 'Rp 150.000'},
        {'id': 6, 'category': 'Home Cleaning', 'subcategory': 'Regular Cleaning', 'status': 'Pesanan Dibatalkan', 'alamat': 'Jl. Mawar No. 3', 'tanggal': '2024-05-20', 'waktu': '13:00', 'harga': 'Rp 150.000'},
        {'id': 7, 'category': 'Gardening', 'subcategory': 'Lawn Mowing', 'status': 'Menunggu Pekerja Berangkat', 'alamat': 'Jl. Tulip No. 8', 'tanggal': '2024-05-22', 'waktu': '09:00', 'harga': 'Rp 100.000'},
    ]

# Variabel global untuk menyimpan data dummy service orders
SERVICE_ORDERS = get_dummy_job_orders()

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

    filtered_orders = [order for order in SERVICE_ORDERS if order['status'] == 'Menunggu Pekerja Berangkat']

    if selected_category:
        filtered_orders = [order for order in filtered_orders if order['category'] == selected_category]
        if selected_subcategory:
            filtered_orders = [order for order in filtered_orders if order['subcategory'] == selected_subcategory]

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        for order in SERVICE_ORDERS:
            if order['id'] == int(order_id):
                order['status'] = 'Pekerja Tiba Di Lokasi'
                break
        return redirect('service_orders')

    context = {
        'user': user,
        'service_orders': filtered_orders,
        'categories': list(set(order['category'] for order in SERVICE_ORDERS)),
        'subcategories': list(set(order['subcategory'] for order in SERVICE_ORDERS if order['category'] == selected_category)) if selected_category else []
    }
    return render(request, 'mypay/service_orders.html', context)

# @login_required
def status_pekerjaan(request):
    worker = get_dummy_worker()
    
    global SERVICE_ORDERS

    selected_status = request.GET.get('status')
    selected_name = request.GET.get('name')

    # Filter orders assigned to the worker
    worker_orders = [order for order in SERVICE_ORDERS if order['status'] in ['Pekerja Tiba Di Lokasi', 'Pelayanan Jasa Sedang Dilakukan', 'Pesanan Selesai']]

    if selected_status:
        worker_orders = [order for order in worker_orders if order['status'] == selected_status]
    if selected_name:
        worker_orders = [order for order in worker_orders if selected_name.lower() in order['category'].lower()]

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        action = request.POST.get('action')
        for order in SERVICE_ORDERS:
            if order['id'] == int(order_id):
                if action == 'arrived':
                    order['status'] = 'Pekerja Tiba Di Lokasi'
                elif action == 'servicing':
                    order['status'] = 'Pelayanan Jasa Sedang Dilakukan'
                elif action == 'completed':
                    order['status'] = 'Pesanan Selesai'
                break
        return redirect('status_pekerjaan')

    context = {
        'worker': worker,
        'service_orders': worker_orders,
        'statuses': list(set(order['status'] for order in worker_orders)),
        'names': list(set(order['category'] for order in worker_orders))
    }
    return render(request, 'mypay/status_pekerjaan.html', context)