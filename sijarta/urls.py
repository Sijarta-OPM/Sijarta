from django.contrib import admin
from django.urls import path, include
from authentication.views import login_view  # Impor login_view dari authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', login_view, name='login'),  # Path login yang unik
    path('auth/', include('authentication.urls')),  # Path lain untuk autentikasi
    path('', include('homepage.urls')),  # Homepage diatur sebagai root URL
    path('jasa/', include('jasa.urls')),  # URL untuk app jasa
    path('voucher/', include('pembelian_voucher.urls')),
    path('testimoni/', include('testimoni.urls')),
    path('mypay/', include('mypay.urls')),  # Menambahkan URL untuk mypay
]
