from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm

from reservations.models import Booking
from .forms import CustomUserCreationForm

User = get_user_model()


#  Регистрация пользователя
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически логиним после регистрации
            messages.success(request, "Регистрация прошла успешно! Добро пожаловать!")
            return redirect("users:my_bookings")
        else:
            messages.error(request, "Ошибка регистрации. Проверьте введенные данные.")
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


#  Вход в систему
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Вы успешно вошли!")
            return redirect("reservations:my_bookings")
        else:
            messages.error(request, "Неверное имя пользователя или пароль.")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


#  Личный кабинет пользователя
def profile_view(request):
    return render(request, "profile.html")


#  Выход из системы
def logout_view(request):
    logout(request)
    messages.success(request, "Вы вышли из системы! Возвращайтесь снова!")
    return redirect("login")  # Перенаправляем на страницу входа


@login_required
def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "my_bookings.html", {"bookings": bookings})
