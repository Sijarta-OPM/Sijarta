from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import PemesananForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def subkategori_detail(request, subkategori_id):
    # Ambil data subkategori
    subkategori = get_object_or_404(Subkategori, pk=subkategori_id)
    sesi_list = SesiLayanan.objects.filter(subkategori=subkategori)
    pekerja_list = Pekerja.objects.all()  # Ambil pekerja yang tersedia untuk subkategori ini

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
            pemesanan.total_pembayaran = sesi.harga  # Set total pembayaran sesuai harga sesi
            pemesanan.save()
            return HttpResponseRedirect('/jasa/pemesanan/')  # Redirect ke halaman daftar pemesanan
    else:
        form = PemesananForm()

    return render(request, 'buat_pemesanan.html', {
        'form': form,
        'sesi': sesi,
        'total_pembayaran': sesi.harga,  # Kirim harga untuk ditampilkan di template
    })

# List Pemesanan
@login_required
def list_pemesanan(request):
    # Get orders for the logged-in user only
    pemesanan_list = Pemesanan.objects.filter(user=request.user).select_related('sesi', 'sesi__subkategori', 'pekerja')

    return render(request, 'list_pemesanan.html', {
        'pemesanan_list': pemesanan_list,
    })
