from django.db import models
from django.contrib.auth.models import User
# Create your models here.

SIZES = (
    ('X', 'Extra Small'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('I', 'Extra Large'),
)

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  description = models.TextField(max_length=250)
  size = models.CharField(
    max_length=1,
    choices=SIZES,
    default=SIZES[0][0]
  )
  quantity = models.IntegerField()
  category = models.TextField(max_length=100)

