from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from reservations.views import home, about, booking_view, contact_view, TableViewSet, BookingViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Restaurant Booking API",
        default_version='v1',
        description="API для бронирования столиков в ресторане",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@restaurant.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
router = DefaultRouter()
router.register(r'tables', TableViewSet, basename='table')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('booking/', booking_view, name='booking'),
    path('users/', include('users.urls')),
    path("contact/", contact_view, name="contact"),
    path('api/', include(router.urls)),
    path("api/v1/reservations/", include("reservations.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc-ui"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)