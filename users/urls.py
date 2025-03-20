from django.urls import path
from .views import register_view, login_view, profile_view, my_bookings_view
from django.contrib.auth.views import LogoutView

app_name = "users"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
    path("my_bookings/", my_bookings_view, name="my_bookings"),
]
