from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import PemesananForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def subkategori_detail(request, subkategori_id):
    # Ambil data subkategori
    subkategori = get_object_or_404(Subkategori, pk=subkategori_id)
    sesi_list = SesiLayanan.objects.filter(subkategori=subkategori)
    pekerja_list = Pekerja.objects.all()  # Dummy data pekerja

    # Tentukan role (pengguna atau pekerja)
    is_pekerja = request.user.groups.filter(name='Pekerja').exists() if request.user.is_authenticated else False

    return render(request, 'subkategori_detail.html', {
        'subkategori': subkategori,
        'sesi_list': sesi_list,
        'pekerja_list': pekerja_list,
        'is_pekerja': is_pekerja,
    })

# Buat Pemesanan
@login_required
def buat_pemesanan(request, sesi_id):
    sesi = get_object_or_404(SesiLayanan, pk=sesi_id)
    if request.method == 'POST':
        form = PemesananForm(request.POST)
        if form.is_valid():
            pemesanan = form.save(commit=False)
            pemesanan.sesi = sesi
            pemesanan.save()
            return HttpResponseRedirect('/jasa/pemesanan/')  # Redirect ke list pemesanan
    else:
        form = PemesananForm()

    return render(request, 'buat_pemesanan.html', {'form': form, 'sesi': sesi})

# List Pemesanan
def list_pemesanan(request):
    # Ambil data subkategori untuk filter
    subkategori_list = Subkategori.objects.all()

    # Ambil semua pemesanan (bisa ditambah filter jika diperlukan)
    pemesanan_list = Pemesanan.objects.select_related('sesi', 'sesi__subkategori', 'pekerja')

    return render(request, 'list_pemesanan.html', {
        'subkategori_list': subkategori_list,
        'pemesanan_list': pemesanan_list,
    })
