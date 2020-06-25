from django.contrib import admin
from .models import Product, Order, Cause, Profile, ProductPhoto, CausePhoto

# Register your models here.
admin.site.register(Product)

admin.site.register(Order)

admin.site.register(Cause)

admin.site.register(Profile)

admin.site.register(ProductPhoto)

admin.site.register(CausePhoto)

