from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True, verbose_name="Номер столика")
    seats = models.PositiveIntegerField(verbose_name="Количество мест")

    def __str__(self):
        return f"Столик {self.number} ({self.seats} мест)"

    class Meta:
        verbose_name = "Столик"
        verbose_name_plural = "Столики"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждено'),
        ('rejected', 'Отклонено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name="Имя клиента", default="Неизвестный")
    phone = models.CharField(max_length=20, verbose_name="Телефон", default="Нет телефона")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, verbose_name="Столик")
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")
    guests = models.PositiveIntegerField(verbose_name="Количество гостей")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="Статус брони")

    def __str__(self):
        return f"Бронь {self.name} на {self.date} в {self.time}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"



class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название ресторана")
    description = models.TextField(verbose_name="Описание")
    address = models.CharField(max_length=255, default="Не указан", verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон", default="+7 898 176 54 67")
    email = models.EmailField(verbose_name="Email", default="info@example.com")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация о ресторане"
        verbose_name_plural = "Информация о ресторане"


class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    position = models.CharField(max_length=100, verbose_name="Должность")
    photo = models.ImageField(upload_to="team_photos/", verbose_name="Фото")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Команда"


class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название блюда")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="menu_images/", verbose_name="Фото блюда", default="menu_images/default.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Меню"



class HomePageContent(models.Model):
    """Модель для редактирования главной страницы"""
    welcome_text = models.CharField(max_length=255, verbose_name="Приветственный текст")
    description = models.TextField(verbose_name="Описание ресторана")
    background_image = models.ImageField(upload_to="homepage_images/", verbose_name="Фон главной страницы", null=True,
                                         blank=True)

    def __str__(self):
        return "Контент главной страницы"

    class Meta:
        verbose_name = "Контент главной страницы"
        verbose_name_plural = "Контент главной страницы"
