from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Statie


class StatieAdmin(admin.ModelAdmin):
    list_display = ["nume", "StatieID", "long", "lat"]


admin.site.register(Statie, StatieAdmin)
