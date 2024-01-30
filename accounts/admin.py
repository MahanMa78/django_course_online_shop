from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomChangeForm,CustomUserCreationForm
from .models import CustomUser

# @admin.register(CustomUser) --> yek rahe hal ham ine
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomChangeForm
    list_display = ['username','email',]
    

# Register your models here.
admin.site.register(CustomUser,CustomUserAdmin)