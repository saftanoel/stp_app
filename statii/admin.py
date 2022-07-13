from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Statie, Autobuz


class StatieAdmin(admin.ModelAdmin):
    list_display = ["nume", "StatieID", "long", "lat"]


class AutobuzAdmin(admin.ModelAdmin):
    list_display = ["nrInm", "idBus", "long", "lat"]


admin.site.register(Statie, StatieAdmin)
admin.site.register(Autobuz, AutobuzAdmin)
