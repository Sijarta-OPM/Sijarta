from django.shortcuts import render
from jasa.models import Kategori, Subkategori

def homepage(request):
    # Ambil semua kategori
    kategori_list = Kategori.objects.all()

    # Filter berdasarkan GET parameter
    kategori_id = request.GET.get('kategori', '')
    search_query = request.GET.get('search', '')

    if kategori_id:
        kategori_list = kategori_list.filter(id=kategori_id)

    if search_query:
        kategori_list = kategori_list.filter(subkategori__nama__icontains=search_query).distinct()

    return render(request, 'homepage.html', {
        'kategori_list': kategori_list,
    })
