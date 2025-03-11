from django import forms
from .models import Booking, Table

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["table", "date", "time", "guests"]
        widgets = {
            "table": forms.Select(attrs={"class": "form-select"}),  # Выбор столика
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "guests": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
        }
        labels = {
            "table": "Выберите столик",
            "date": "Дата бронирования",
            "time": "Время бронирования",
            "guests": "Количество гостей",
        }

    def clean_guests(self):
        guests = self.cleaned_data.get("guests")
        if guests < 1:
            raise forms.ValidationError("Количество гостей должно быть не менее 1.")
        return guests
