from django.test import TestCase
from reservations.models import Table, Booking, User
from reservations.serializers import TableSerializer, BookingSerializer
from datetime import date, time


class TableSerializerTest(TestCase):
    def test_table_serializer_valid_data(self):
        """Проверка сериализации модели Table"""
        table = Table.objects.create(number=1, seats=4)
        serializer = TableSerializer(table)
        expected_data = {"id": table.id, "number": 1, "seats": 4}
        self.assertEqual(serializer.data, expected_data)


class BookingSerializerTest(TestCase):
    def setUp(self):
        """Создание тестовых данных"""
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.table = Table.objects.create(number=2, seats=2)

    def test_booking_serializer_valid_data(self):
        """Проверка сериализации модели Booking"""
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            date=date.today(),
            time=time(18, 0),
            guests=2,
            status="pending",
        )
        serializer = BookingSerializer(booking)
        expected_data = {
            "id": booking.id,
            "user": self.user.id,
            "table": self.table.id,
            "date": str(date.today()),
            "time": "18:00:00",
            "guests": 2,
            "status": "pending",
        }
        self.assertEqual(serializer.data, expected_data)
