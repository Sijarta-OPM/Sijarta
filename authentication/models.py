from django.contrib.auth.models import User
from django.db import models

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userdata')
    no_hp = models.CharField(max_length=15, unique=True)
    alamat = models.TextField(blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    role = models.CharField(
        max_length=10,
        choices=[('PENGGUNA', 'Pengguna'), ('PEKERJA', 'Pekerja')],
        default='PENGGUNA'
    )
    nama_bank = models.CharField(max_length=50, blank=True, null=True)
    nomor_rekening = models.CharField(max_length=20, blank=True, null=True)
    npwp = models.CharField(max_length=20, blank=True, null=True)
    link_foto = models.URLField(blank=True, null=True)
