from django.contrib import admin
from src.apps.cars.models import Car, Color, Brand, Model, Picture

admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Picture)
