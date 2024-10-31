from django.contrib import admin
from account.models import User

# Register your models here.
class AdminUser(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'is_active',
        'role',
        'date_joined',
    ]


admin.site.register(User,AdminUser)