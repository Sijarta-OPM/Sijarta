from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
import uuid
from django.contrib import messages
from django.db import connection

def login_view(request):
    if request.method == 'POST':
        no_hp = request.POST.get('no_hp')
        pwd = request.POST.get('password')

        # Cek apakah No HP dan password cocok dengan data di database
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM SIJARTA."USER" WHERE no_hp = %s
            """, [no_hp])
            row = cursor.fetchone()

            if row:
                user = dict(zip([column[0] for column in cursor.description], row))
                # Cek password
                if pwd == user.get('password'):
                    request.session['user'] = user  # Menyimpan data pengguna dalam sesi
                    request.session.save()
                    return redirect('kuning:landing')  # Redirect ke halaman landing atau dashboard
                else:
                    messages.error(request, "Password salah!")
            else:
                messages.error(request, "No HP tidak terdaftar!")

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')  # Menangkap role yang dipilih
        id = uuid.uuid4()
        nama = request.POST.get('nama')
        password = request.POST.get('password')
        jenis_kelamin = request.POST.get('jenis_kelamin')
        no_hp = request.POST.get('no_hp')
        tanggal_lahir = request.POST.get('tanggal_lahir')
        alamat = request.POST.get('alamat')

        # # Cek apakah No HP sudah terdaftar
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM SIJARTA."USER" WHERE no_hp = %s
            """, [no_hp])
            row = cursor.fetchone()

            if row:
                # Jika nomor HP sudah ada, tampilkan pesan dan redirect ke login
                messages.error(request, "No HP sudah terdaftar. Silakan login.")
                return redirect('authentication:login')

        # Jika No HP unik, simpan data pengguna baru
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO SIJARTA."USER" (id, nama, jenis_kelamin, no_hp, password, tanggal_lahir, alamat)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, [id, nama, jenis_kelamin, no_hp, password, tanggal_lahir, alamat])

            if role == 'PELANGGAN':
                cursor.execute("""
                    INSERT INTO SIJARTA.PELANGGAN (id, level)
                    VALUES (%s, 'Basic')
                """, [id])
            
            elif role == 'PEKERJA':
                nama_bank = request.POST.get('nama_bank')
                nomor_rekening = request.POST.get('nomor_rekening')
                npwp = request.POST.get('npwp')
                link_foto = request.POST.get('link_foto')
                cursor.execute("""
                    INSERT INTO SIJARTA.PEKERJA (id, nama_bank, nomor_rekening, npwp, link_foto)
                    VALUES (%s, %s, %s, %s, %s)
                """, [id, nama_bank, nomor_rekening, npwp, link_foto])

        return redirect('authentication:login')  # Setelah berhasil, arahkan ke login
    
    return render(request, 'register.html')

def logout_view(request):
    request.session.flush()  # Menghapus semua data session
    return redirect('authentication:login')
