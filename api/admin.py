from django.contrib import admin

from api.models import Product, Order, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Category)
