from django.contrib import admin
from django.urls import path

from shop.views import MainPage, CustomLoginView, RegisterView, logout_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("", MainPage.as_view(), name="index"),
]
