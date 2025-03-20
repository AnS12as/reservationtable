# Используем Python 3.10
FROM python:3.10

# Переменная для отключения буферизации вывода
ENV PYTHONUNBUFFERED=1

# Создаём рабочую директорию
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app/

# Запускаем Gunicorn
CMD ["gunicorn", "restaurant_booking.wsgi:application", "--bind", "0.0.0.0:8000"]
