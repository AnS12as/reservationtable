📌 README.md (короткий вариант)
# 🍽 Reservation Table - Бронирование столиков

**Reservation Table** — это веб-приложение на **Django**, предназначенное для онлайн-бронирования столиков в ресторане.  
Используется **PostgreSQL, Docker, Gunicorn, Nginx** и **автоматический деплой через GitHub Actions**.

---

## 🚀 Запуск локально

### 1️⃣ Клонировать репозиторий:
```sh
git clone https://github.com/AnS12as/reservationtable.git
cd reservationtable

2️⃣ Создать виртуальное окружение:

python3 -m venv venv
source venv/bin/activate  # macOS/Linux

3️⃣ Установить зависимости:
pip install -r requirements.txt

4️⃣ Запустить сервер:
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Открыть: http://127.0.0.1:8000/

🐳 Запуск через Docker

1️⃣ Создать .env файл:
POSTGRES_DB=restaurant_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=adminpassword
POSTGRES_HOST=db
POSTGRES_PORT=5432
DJANGO_SECRET_KEY=your_secret_key
DEBUG=False
2️⃣ Запустить проект в Docker:
docker-compose up -d --build
Теперь сайт доступен по http://localhost.

☁ Деплой на Yandex Cloud

1️⃣ Подключиться к серверу:
ssh user@your-server-ip
2️⃣ Клонировать репозиторий:
git clone https://github.com/AnS12as/reservationtable.git
cd reservationtable
3️⃣ Запустить в Docker:
docker-compose up -d --build
🔄 Автоматический деплой (GitHub Actions)

При каждом git push в main, код автоматически деплоится.
Добавь в GitHub секретные переменные (Settings → Secrets):

YC_SSH_USER = user
YC_SERVER_IP = 84.201.150.100
🔐 Установка HTTPS (SSL)

sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com
Теперь сайт работает по HTTPS.

✅ Автоматическое форматирование кода

pip install black flake8
black .
flake8 .
📜 Лицензия: MIT
🎉 Проект готов к работе! 🚀


