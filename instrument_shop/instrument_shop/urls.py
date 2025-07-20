from django.contrib import admin
from django.urls import path

from shop.views import MainPage, CustomLoginView, RegisterView, logout_view
from admin_panel.views import admin_dashboard

from shop.models import Instrument, Category
from users.models import User


admin.site.register(Instrument)
admin.site.register(Category)
admin.site.register(User)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("", MainPage.as_view(), name="index"),
    # 
    path("adminpanel/", admin_dashboard, name="admin_dashboard"),
]
