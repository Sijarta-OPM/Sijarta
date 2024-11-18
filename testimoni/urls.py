from django.urls import path
from .views import testimoni

app_name = 'testimoni'

urlpatterns = [
    path('', testimoni, name='testimoni_form'),
]