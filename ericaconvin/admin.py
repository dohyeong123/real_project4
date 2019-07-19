from django.contrib import admin
from .models import Restaurant
from .models import Category

admin.site.register(Restaurant)
admin.site.register(Category)