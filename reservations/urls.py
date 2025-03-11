from django.urls import path
from .views import (
    home, about, booking_view, reservation_list,
    confirm_booking, reject_booking, cancel_booking,
    edit_booking, my_bookings_view, contact_view
)

app_name = "reservations"

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('booking/', booking_view, name='booking'),
    path("list/", reservation_list, name="reservation_list"),
    path("contact/", contact_view, name="contact"),

    path("confirm-booking/<int:booking_id>/", confirm_booking, name="confirm_booking"),
    path("reject-booking/<int:booking_id>/", reject_booking, name="reject_booking"),
    path("edit-booking/<int:booking_id>/", edit_booking, name="edit_booking"),
    path("cancel-booking/<int:booking_id>/", cancel_booking, name="cancel_booking"),
    path("my_bookings/", my_bookings_view, name="my_bookings"),
]
