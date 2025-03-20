from django.test import TestCase
from django.contrib.auth import get_user_model
from reservations.models import (
    Table,
    Booking,
    RestaurantInfo,
    TeamMember,
    MenuItem,
    HomePageContent,
)
from datetime import date, time
from decimal import Decimal

User = get_user_model()


class TableModelTest(TestCase):
    def setUp(self):
        self.table = Table.objects.create(number=1, seats=4)

    def test_table_creation(self):
        """Проверяем, создается ли столик"""
        self.assertEqual(self.table.number, 1)
        self.assertEqual(self.table.seats, 4)

    def test_table_str(self):
        """Проверяем строковое представление модели Table"""
        self.assertEqual(str(self.table), "Столик 1 (4 мест)")


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.table = Table.objects.create(number=2, seats=6)

        print(f"Создан пользователь: {self.user} (username: {self.user.username})")

        self.booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            date=date.today(),
            time=time(18, 30),
            guests=3,
            status="pending",
        )

        # Принудительно загружаем объект из базы данных
        self.booking.refresh_from_db()

        print(f"Создана бронь: {self.booking} (user: {self.booking.user})")

    def test_booking_creation(self):
        """Проверяем, создается ли бронирование"""
        self.booking.refresh_from_db()  # Перезагружаем объект
        self.assertIsNotNone(self.booking.user, "Пользователь не должен быть None")
        self.assertEqual(self.booking.user.username, "testuser")
        self.assertEqual(self.booking.table.number, 2)
        self.assertEqual(self.booking.guests, 3)
        self.assertEqual(self.booking.status, "pending")

    def test_booking_str(self):
        """Проверяем строковое представление модели Booking"""
        self.booking.refresh_from_db()  # Перезагружаем объект

        print(f"В тесте booking.user: {self.booking.user} (username: {self.booking.user.username if self.booking.user else 'None'})")

        expected_str = f"Бронь {self.booking.user.username} на {self.booking.date} в {self.booking.time}"
        actual_str = str(self.booking)
        self.assertEqual(actual_str, expected_str, f"Ожидалось: {expected_str}, но получено: {actual_str}")


class RestaurantInfoModelTest(TestCase):
    def setUp(self):
        self.restaurant = RestaurantInfo.objects.create(
            name="Тестовый ресторан",
            description="Описание ресторана",
            address="Улица Тестовая, 123",
            phone="+7 999 888 77 66",
            email="test@example.com",
        )

    def test_restaurant_creation(self):
        """Проверяем, создается ли информация о ресторане"""
        self.assertEqual(self.restaurant.name, "Тестовый ресторан")
        self.assertEqual(self.restaurant.phone, "+7 999 888 77 66")

    def test_restaurant_str(self):
        """Проверяем строковое представление модели RestaurantInfo"""
        self.assertEqual(str(self.restaurant), "Тестовый ресторан")


class TeamMemberModelTest(TestCase):
    def setUp(self):
        self.team_member = TeamMember.objects.create(
            name="Иван Иванов", position="Шеф-повар", photo="team_photos/chef.jpg"
        )

    def test_team_member_creation(self):
        """Проверяем, создается ли член команды"""
        self.assertEqual(self.team_member.name, "Иван Иванов")
        self.assertEqual(self.team_member.position, "Шеф-повар")

    def test_team_member_str(self):
        """Проверяем строковое представление модели TeamMember"""
        self.assertEqual(str(self.team_member), "Иван Иванов")


class MenuItemModelTest(TestCase):
    def setUp(self):
        self.menu_item = MenuItem.objects.create(
            name="Паста",
            description="Вкусная паста",
            image="menu_images/pasta.jpg",
            price=Decimal("599.99"),
        )

    def test_menu_item_creation(self):
        """Проверяем, создается ли пункт меню"""
        self.assertEqual(self.menu_item.name, "Паста")
        self.assertEqual(self.menu_item.price, Decimal("599.99"))

    def test_menu_item_str(self):
        """Проверяем строковое представление модели MenuItem"""
        self.assertEqual(str(self.menu_item), "Паста")


class HomePageContentModelTest(TestCase):
    def setUp(self):
        self.homepage_content = HomePageContent.objects.create(
            welcome_text="Добро пожаловать!",
            description="Лучший ресторан в городе",
            background_image="homepage_images/bg.jpg",
        )

    def test_homepage_content_creation(self):
        """Проверяем, создается ли контент главной страницы"""
        self.assertEqual(self.homepage_content.welcome_text, "Добро пожаловать!")
        self.assertEqual(self.homepage_content.description, "Лучший ресторан в городе")

    def test_homepage_content_str(self):
        """Проверяем строковое представление модели HomePageContent"""
        self.assertEqual(str(self.homepage_content), "Контент главной страницы")
