from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserData
from django.contrib.auth import logout
from datetime import date

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

        # Validasi data wajib
        if not username or not password or not nama or not no_hp or not alamat or not tanggal_lahir:
            messages.error(request, "Semua field wajib diisi!")
            return render(request, 'register.html')

        # Validasi username unik
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username sudah digunakan!")
            return render(request, 'register.html')

        # Validasi nomor HP unik
        if UserData.objects.filter(no_hp=no_hp).exists():
            messages.error(request, "Nomor HP sudah digunakan!")
            return render(request, 'register.html')

        # Validasi tanggal lahir
        try:
            if date.fromisoformat(tanggal_lahir) > date.today():
                messages.error(request, "Tanggal lahir tidak valid!")
                return render(request, 'register.html')
        except ValueError:
            messages.error(request, "Format tanggal lahir tidak valid!")
            return render(request, 'register.html')

        try:
            # Buat user baru
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=nama
            )

            # Cek role dan simpan data
            if role == "PEKERJA":
                nama_bank = request.POST.get('nama_bank')
                nomor_rekening = request.POST.get('nomor_rekening')
                npwp = request.POST.get('npwp')
                link_foto = request.POST.get('link_foto')
                UserData.objects.create(
                    user=user,
                    no_hp=no_hp,
                    alamat=alamat,
                    tanggal_lahir=tanggal_lahir,
                    role=role,
                    nama_bank=nama_bank,
                    nomor_rekening=nomor_rekening,
                    npwp=npwp,
                    link_foto=link_foto
                )
            else:  # Untuk PENGGUNA
                UserData.objects.create(
                    user=user,
                    no_hp=no_hp,
                    alamat=alamat,
                    tanggal_lahir=tanggal_lahir,
                    role=role
                )

            messages.success(request, "Akun berhasil dibuat!")
            return redirect('authentication:login')
        except Exception as e:
            messages.error(request, f"Terjadi kesalahan: {e}")
            return render(request, 'register.html')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifikasi kredensial pengguna
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirect ke halaman utama
        else:
            messages.error(request, "Username atau password salah!")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Menghapus sesi pengguna
    return redirect('authentication:login')
