from django.contrib import admin
from .models import UserM
# Register your models here.
class StudenAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

# class SignupAdmin(admin.ModelAdmin):
#     list_display = ('name', 'first_name', 'last_name', 'email')

admin.site.register(UserM, StudenAdmin)