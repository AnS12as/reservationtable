from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets, permissions
from .models import Table, Booking, RestaurantInfo, TeamMember, HomePageContent, MenuItem
from .serializers import TableSerializer, BookingSerializer
from .forms import BookingForm


# Главная страница
def home(request):
    homepage_content = HomePageContent.objects.first()
    menu_items = MenuItem.objects.all()
    return render(request, 'home.html', {
        "homepage_content": homepage_content,
        "menu_items": menu_items
    })


def contact_view(request):
    return render(request, "contact.html")


# О нас
def about(request):
    restaurant_info = RestaurantInfo.objects.first()
    team_members = TeamMember.objects.all()
    return render(request, "reservations/about.html", {
        "restaurant_info": restaurant_info,
        "team_members": team_members
    })


# Список бронирований (для администратора)
@login_required
def reservation_list(request):
    bookings = Booking.objects.all()
    return render(request, "reservations/reservation_list.html", {"bookings": bookings})


# Функция бронирования
@login_required
def booking_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.status = "pending"
            booking.save()
            messages.success(request, f"Спасибо за бронирование! Мы ждем вас {booking.date} в {booking.time}.")
            return redirect("reservations:my_bookings")
    else:
        form = BookingForm()

    tables = Table.objects.all()
    return render(request, "booking.html", {"form": form, "tables": tables})


# Страница "Мои бронирования"

def my_bookings_view(request):
    bookings = Booking.objects.filter(user=request.user)
    print("Бронирования пользователя:", bookings)  # Debug
    return render(request, "reservations/my_bookings.html", {"bookings": bookings})



# Подтверждение бронирования (администратор)
@login_required
def confirm_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = "confirmed"
    booking.save()
    messages.success(request, "✅ Бронирование подтверждено!")
    return redirect("reservations:reservation_list")


# Отклонение бронирования (администратор)
@login_required
def reject_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.status = "rejected"
    booking.save()
    messages.error(request, "❌ Бронирование отклонено.")
    return redirect("reservations:reservation_list")


# Отмена бронирования (пользователь)
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, "✅ Ваше бронирование успешно отменено.")
    return redirect("reservations:my_bookings")


# Изменение бронирования (пользователь)
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Бронирование успешно обновлено!")
            return redirect("reservations:my_bookings")
    else:
        form = BookingForm(instance=booking)

    return render(request, "reservations/edit_booking.html", {"form": form, "booking": booking})


# API ViewSets
class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [permissions.AllowAny]


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
