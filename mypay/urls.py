from django.urls import path
from . import views

urlpatterns = [
    path('', views.mypay_dashboard, name='mypay_dashboard'),
    path('transaction/', views.mypay_transaction, name='mypay_transaction'),
    path('service_orders/', views.service_orders, name='service_orders'),
    path('status_pekerjaan/', views.status_pekerjaan, name='status_pekerjaan'),  # New URL pattern
]