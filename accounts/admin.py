from django.contrib import admin
from .models import Role, User


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "created_at"]
