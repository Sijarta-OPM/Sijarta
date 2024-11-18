from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserData

def register_view(request):
    if request.method == 'POST':
        # Ambil data dari form
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama = request.POST.get('nama')
        no_hp = request.POST.get('no_hp')
        alamat = request.POST.get('alamat')
        tanggal_lahir = request.POST.get('tanggal_lahir')
        role = request.POST.get('role')

        # Buat user baru
        user = User.objects.create_user(
            username=username,  # Gunakan username sebagai unique identifier
            password=password,
            first_name=nama
        )

        # Buat UserData terkait user
        UserData.objects.create(
            user=user,
            no_hp=no_hp,
            alamat=alamat,
            tanggal_lahir=tanggal_lahir,
            role=role
        )

        messages.success(request, "Akun berhasil dibuat!")
        return redirect('authentication:login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifikasi kredensial pengguna
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('kuning:landing')  # Redirect ke halaman utama
        else:
            messages.error(request, "Username atau password salah!")

    return render(request, 'login.html')
