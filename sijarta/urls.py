from django.contrib import admin
from django.urls import path, include
from authentication.views import login_view  # Impor login_view dari authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('', include('biru.urls')),
    path('', login_view, name='home'),  # Menambahkan URL root yang mengarah ke login_view
]
