from django.db import models
from django.contrib.auth.models import User
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
    price = models.FloatField() #Changed this to float feild
    description = models.TextField(max_length=250)
    size = models.CharField(max_length=100)
    quantity = models.IntegerField()
    category = models.CharField( #made this a choice field choice fields accesed by item.get_category_display
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_CHOICES[0][0]
    )
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

    def __str__(self): #added this string method
        return self.name


class OrderProduct(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_quantity = models.IntegerField(default=1) # this will hold quantity of
    size = models.CharField(  
        max_length=2,
        choices=SIZES,
        default=SIZES[0][0]
    )
    # cart = models.ForeignKey(Cart, on_delete=models.SET_NULL)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self): #added this string method
        return self.item

class Cart(models.Model):
	items = models.ManyToManyField(OrderProduct)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date= models.DateTimeField()
	ordered = models.BooleanField(default=False) #when this true we create new cart
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    #image

	# def __str__(self):
	# 	return self.user.username




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    causes = models.ManyToManyField(Cause)
    #null=True, blank=True

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


