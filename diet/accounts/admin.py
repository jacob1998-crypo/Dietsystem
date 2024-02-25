from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('id','first_name', 'last_name', 'username', 'phone', 'email')

# Register your CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
