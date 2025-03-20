from celery import shared_task
from django.core.mail import send_mail
from .models import Booking
from django.utils.timezone import now, timedelta


@shared_task
def send_booking_reminders():
    """Отправляет напоминания о предстоящих бронированиях"""
    upcoming_bookings = Booking.objects.filter(date=now().date() + timedelta(days=1))

    for booking in upcoming_bookings:
        send_mail(
            "Напоминание о бронировании",
            f"Здравствуйте, {booking.user.username}! Ваше бронирование на {booking.date} в {booking.time}.",
            "noreply@example.com",
            [booking.user.email],
            fail_silently=False,
        )
    return f"Отправлено {upcoming_bookings.count()} напоминаний"
