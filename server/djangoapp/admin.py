from django.contrib import admin
from .models import CarMake, CarModel


# Inline admin to view car models under their make
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1


# Customize CarMake Admin
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    inlines = [CarModelInline]


# Register both models
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)
