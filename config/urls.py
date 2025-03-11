from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from reservations.views import home, about, booking_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('booking/', booking_view, name='booking'),
    path('users/', include('users.urls')),
    path("contact/", contact_view, name="contact"),

    path('', include('reservations.urls', namespace='reservations')),  # ✅ Обрати внимание на `namespace`

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
