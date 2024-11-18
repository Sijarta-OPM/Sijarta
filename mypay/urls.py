from django.urls import path
from . import views

urlpatterns = [
    path('', views.mypay_dashboard, name='mypay_dashboard'),
    path('transaction/', views.mypay_transaction, name='mypay_transaction'),
]