from django.contrib import admin

# Register your models here.
from .models import Receipt,Product
admin.site.register(Receipt)
admin.site.register(Product)