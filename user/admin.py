from django.contrib import admin

from user.models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_display_links = (
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
    )
    list_filter = [
        "is_active",
    ]
    list_per_page = 25


admin.site.register(UserAccount, UserAccountAdmin)
