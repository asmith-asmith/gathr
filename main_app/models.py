from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

SIZES = (
    ('XS', 'Extra Small'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'Extra Large'),
)

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
	('OW', 'Outerwear'),
	('SW', 'Sweatshirt'),
)

class Cause(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    cause_type = models.CharField(max_length=100)
    proceeds = models.IntegerField()
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=100)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_CHOICES[0][0]
    )
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

class CausePhoto(models.Model):
    url = models.CharField(max_length=200)
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cause_id: {self.cause_id} @{self.url}"

class ProductPhoto(models.Model):
    url = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for product_id: {self.product_id} @{self.url}"

class UserPhoto(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for user_id: {self.user_id} @{self.url}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    causes = models.ManyToManyField(Cause)
    purchased_items = models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username


# User model
    # username
    # first_name
    # last_name
    # email
    # password
    # groups
    # is_superuser(boolean)


# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Profile, on_delete=models.SET_NULL)
#     order = models.ForeignKey(Cart, on_delete=models.SET_NULL)
#     address = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)
#     state = models.CharField(max_length=200)
#     zipcode = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str_(self):
#         return self.address


