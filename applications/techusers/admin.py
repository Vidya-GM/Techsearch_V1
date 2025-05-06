from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TechUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = TechUser

    list_display = ('username', 'email', 'last_login')

    readonly_fields = ('created_at', 'updated_at')

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {'fields': ('date_of_birth', 'created_at', 'updated_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )


admin.site.register(TechUser, CustomUserAdmin)