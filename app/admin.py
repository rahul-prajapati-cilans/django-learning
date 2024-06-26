from django.contrib import admin
from .models import Profile

# Register your models here.

# admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "state", "country", "pincode")
