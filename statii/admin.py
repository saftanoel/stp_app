from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Statie


class StatiiAdmin(admin.ModelAdmin):
    list_display = ["nume", "long", "lat"]


admin.site.register(Statie)
