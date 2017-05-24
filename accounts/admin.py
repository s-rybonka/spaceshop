from django.contrib import admin

from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'username')

admin.site.register(Account, AccountAdmin)
