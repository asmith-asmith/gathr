from django.contrib import admin
from .models import Product, Order, Cause, Profile, ProductPhoto

# Register your models here.
admin.site.register(Product)

admin.site.register(Order)

admin.site.register(Cause)

admin.site.register(Profile)

admin.site.register(ProductPhoto)

