from django import forms
from .models import Pemesanan

class PemesananForm(forms.ModelForm):
    class Meta:
        model = Pemesanan
        fields = ['tanggal_pemesanan', 'kode_diskon', 'total_pembayaran', 'metode_pembayaran']
