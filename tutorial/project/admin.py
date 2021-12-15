from django.contrib import admin
from .models import Restaurant, Staff, Country, City, Dish, Menu

admin.site.register(Restaurant)
admin.site.register(Staff)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Dish)
admin.site.register(Menu)