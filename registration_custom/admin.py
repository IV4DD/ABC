from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    list_display = ('first_name', 'middle_name', 'surname', 'email', 'username', 'date_joined', 'last_login')
    search_fields = ('first_name', 'middle_name', 'surname', 'email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)