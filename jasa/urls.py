from django.urls import path
from . import views

urlpatterns = [
    path('subkategori/<int:subkategori_id>/', views.subkategori_detail, name='subkategori'),
    path('pemesanan/buat/<int:sesi_id>/', views.buat_pemesanan, name='buat_pemesanan'),
    path('pemesanan/', views.list_pemesanan, name='list_pemesanan'),
]
