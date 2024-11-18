from django.shortcuts import render
from jasa.models import Kategori, Subkategori

def homepage(request):
    # Ambil semua kategori
    kategori_list = Kategori.objects.prefetch_related('subkategori_set').all()

    # Ambil filter dari GET parameter
    selected_subkategori_id = request.GET.get('kategori', '')

    # Jika subkategori dipilih, filter kategori sesuai subkategori
    if selected_subkategori_id:
        subkategori = Subkategori.objects.filter(id=selected_subkategori_id).first()
        kategori_list = kategori_list.filter(id=subkategori.kategori.id) if subkategori else []

    return render(request, 'homepage.html', {
        'kategori_list': kategori_list,
    })
