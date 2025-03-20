from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "phone", "table", "date", "time", "guests"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ваше имя"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ваш телефон"}
            ),
            "table": forms.Select(attrs={"class": "form-select"}),
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "guests": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        }
        labels = {
            "name": "Имя клиента",
            "phone": "Телефон",
            "table": "Выберите столик",
            "date": "Дата бронирования",
            "time": "Время бронирования",
            "guests": "Количество гостей",
        }
