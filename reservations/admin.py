from django.contrib import admin
from .models import Table, Booking, RestaurantInfo, TeamMember, HomePageContent, MenuItem


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ["number", "seats"]
    search_fields = ["number"]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["user", "date", "time", "table", "status"]
    list_filter = ["status"]
    search_fields = ["user__username", "table__number"]
    actions = ["confirm_booking", "reject_booking"]

    def confirm_booking(self, request, queryset):
        queryset.update(status="confirmed")

    def reject_booking(self, request, queryset):
        queryset.update(status="rejected")


@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    search_fields = ("name", "position")


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ("welcome_text",)
    search_fields = ("welcome_text",)
