from django.db import models

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
    sesi = models.ForeignKey(SesiLayanan, on_delete=models.CASCADE)
    tanggal_pemesanan = models.DateField()
    kode_diskon = models.CharField(max_length=100, blank=True, null=True)
    total_pembayaran = models.DecimalField(max_digits=10, decimal_places=2)
    metode_pembayaran = models.CharField(max_length=50)

    def __str__(self):
        return f'Pemesanan {self.sesi.nama}'
