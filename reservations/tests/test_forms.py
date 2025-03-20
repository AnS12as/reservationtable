from datetime import date, time
from django.test import TestCase
from reservations.forms import BookingForm
from reservations.models import Table, User


class BookingFormTest(TestCase):
    def setUp(self):
        """Создаем тестового пользователя и столик"""
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.table = Table.objects.create(number=1, seats=4)

    def test_valid_form(self):
        """Проверка валидной формы бронирования"""
        form_data = {
            "table": self.table.id,  # ✅ Добавляем ID столика
            "date": date.today(),
            "time": time(18, 30),
            "guests": 2,
        }
        form = BookingForm(data=form_data)

        print(form.errors)  # ✅ Посмотрим, какие ошибки

        self.assertTrue(form.is_valid())  # Ожидаем, что форма будет валидной
