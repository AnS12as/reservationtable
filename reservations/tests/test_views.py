from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from reservations.models import Table, Booking

User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        """Создаём тестовые данные перед каждым тестом"""
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.admin = User.objects.create_superuser(username='admin', password='admin123')

        self.table = Table.objects.create(number=1, seats=4)
        self.booking = Booking.objects.create(
            user=self.user, table=self.table, date="2025-03-15",
            time="18:30", guests=2, status="pending"
        )

    def test_home_page(self):
        """Тест главной страницы"""
        response = self.client.get(reverse('reservations:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page(self):
        """Тест страницы "О нас"."""
        response = self.client.get(reverse('reservations:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations/about.html')

    def test_booking_view_redirects_if_not_logged_in(self):
        """Тест: бронирование требует авторизации"""
        response = self.client.get(reverse('reservations:booking'))
        self.assertEqual(response.status_code, 302)  # Перенаправление на страницу логина

    def test_booking_view_post(self):
        """Тест: успешное бронирование"""
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('reservations:booking'), {
            "table": self.table.id,
            "date": "2025-03-20",
            "time": "19:00",
            "guests": 3
        })
        self.assertEqual(response.status_code, 302)  # Перенаправление после успешного бронирования
        self.assertEqual(Booking.objects.count(), 2)  # Бронирование добавилось

    def test_my_bookings_view(self):
        """Тест страницы 'Мои бронирования'"""
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('reservations:my_bookings'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations/my_bookings.html')

        # Проверяем, есть ли бронирование в таблице
        self.assertContains(response, "March 15, 2025")  # Проверяем дату
        self.assertContains(response, "6:30 p.m.")  # Проверяем время
        self.assertContains(response, "Столик 1 (4 мест)")  # Проверяем столик
        self.assertContains(response, "2")  # Проверяем гостей
        self.assertContains(response, "Ожидает подтверждения")  # Проверяем статус

    def test_edit_booking(self):
        """Тест редактирования бронирования"""
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('reservations:edit_booking', args=[self.booking.id]), {
            "table": self.table.id,
            "date": "2025-03-25",
            "time": "20:00",
            "guests": 4
        })
        self.assertEqual(response.status_code, 302)  # Перенаправление после сохранения
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.date.strftime("%Y-%m-%d"), "2025-03-25")  # Проверяем изменение даты

    def test_cancel_booking(self):
        """Тест отмены бронирования"""
        self.client.login(username='testuser', password='password123')
        response = self.client.post(reverse('reservations:cancel_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 302)  # Перенаправление после отмены
        self.assertEqual(Booking.objects.count(), 0)  # Бронирование удалено

    def test_reservation_list_admin(self):
        """Тест списка бронирований (для админа)"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('reservations:reservation_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservations/reservation_list.html')

        # Проверяем, что бронирование есть в списке
        self.assertContains(response, "March 15, 2025")
        self.assertContains(response, "6:30 p.m.")
        self.assertContains(response, "Столик 1 (4 мест)")
        self.assertContains(response, "2")
        self.assertContains(response, "Ожидает подтверждения")

    def test_confirm_booking(self):
        """Тест подтверждения бронирования админом"""
        self.client.login(username='admin', password='admin123')
        response = self.client.post(reverse('reservations:confirm_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 302)  # Перенаправление
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, "confirmed")  # Проверяем изменение статуса

    def test_reject_booking(self):
        """Тест отклонения бронирования админом"""
        self.client.login(username='admin', password='admin123')
        response = self.client.post(reverse('reservations:reject_booking', args=[self.booking.id]))
        self.assertEqual(response.status_code, 302)  # Перенаправление
        self.booking.refresh_from_db()
        self.assertEqual(self.booking.status, "rejected")  # Проверяем изменение статуса
