from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from.models import coustomUser

# Register your models here.
class CustomerUserAdmin(UserAdmin):
    model = coustomUser
    list_display = ['username','email','its_staff','is_active']
    fieldsets = UserAdmin.fieldsets+(
        ('Extra Info',{'fields':('bio','profile_pic')})


    )

admin.site.register(coustomUser,CustomerUserAdmin)

