from django.urls import path
from authentication.views import login_view
from authentication.views import register_view
from django.contrib.auth.views import LogoutView

app_name = "authentication"

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]