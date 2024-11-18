from django.db import models
from django.contrib.auth.models import User  # Ensure User is imported if using ForeignKey

class Kategori(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama


class Subkategori(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama


class SesiLayanan(models.Model):
    subkategori = models.ForeignKey(Subkategori, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama


class Pekerja(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama


class Pemesanan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Connect to the logged-in user
    sesi = models.ForeignKey(SesiLayanan, on_delete=models.CASCADE)
    pekerja = models.ForeignKey(Pekerja, on_delete=models.SET_NULL, null=True, blank=True)  # Nullable pekerja
    tanggal_pemesanan = models.DateField()
    kode_diskon = models.CharField(max_length=100, blank=True, null=True)
    total_pembayaran = models.DecimalField(max_digits=10, decimal_places=2)
    metode_pembayaran = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=[('Menunggu Pembayaran', 'Menunggu Pembayaran'),
                                                     ('Mencari Pekerja Terdekat', 'Mencari Pekerja Terdekat'),
                                                     ('Pesanan Selesai', 'Pesanan Selesai')], default='Menunggu Pembayaran')

    def __str__(self):
        return f'Pemesanan {self.sesi.nama} oleh {self.user.username}'
