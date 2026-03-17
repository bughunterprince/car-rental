from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("cars/", views.cars, name="cars"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("register/", views.register_page, name="register"),
    path("booking/", views.booking_page, name="booking"),
    path("carsdetail/", views.cars_detail_page, name="carsdetail"),
    path("dashboard/", views.user_dashboard, name="dashboard"),
    path("admindash/", views.admin_dashboard, name="admindash"),
    # Legacy routes so existing links like first.html continue to work.
    path("first.html", views.home),
    path("cars.html", views.cars),
    path("login.html", views.login_page),
    path("logout.html", views.logout_page),
    path("register.html", views.register_page),
    path("booking.html", views.booking_page),
    path("carsdetail.html", views.cars_detail_page),
    path("userdash.html", views.user_dashboard),
    path("admindash.html", views.admin_dashboard),
]
