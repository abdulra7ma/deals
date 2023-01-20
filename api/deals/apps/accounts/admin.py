from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy

from deals.apps.accounts.models import UserAccount


admin.site.unregister(Group)


@admin.register(UserAccount)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("password",)}),
        (gettext_lazy("Personal info"), {"fields": ("username", "first_name", "last_name")}),
        (
            gettext_lazy("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")},
        ),
        (gettext_lazy("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("username", "password1", "password2")}),)
    list_display = ("username", "first_name", "last_name", "is_staff", "is_active")
    search_fields = ("first_name", "last_name", "username")
    ordering = ("username",)
    readonly_fields = ("username",)
