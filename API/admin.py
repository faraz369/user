from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# @admin.register(Blog)
# admin.site.register(Blog)
@admin.register(User)
class UserAdmin(UserAdmin):
    list_display=['username','email','password','is_active','is_staff','is_admin','is_superuser']