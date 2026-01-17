from django.contrib import admin
from .models import Car
from .models import Scooter



class CarAdmin(admin.ModelAdmin):
    list_display = ('brand','model','year', 'price')
    search_fields = ('brand',)
    list_filter = ('brand', 'model', 'year')


class ScooterAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price')
    search_fields = ('brand',)
    list_filter = ('brand', 'model', 'year')


admin.site.register(Car, CarAdmin)
admin.site.register(Scooter, ScooterAdmin)