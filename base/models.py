from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class ProductsModel(models.Model):
    product_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=100)
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(default='default.jpeg', upload_to='uploads')
    trending = models.BooleanField(default=False)
    offer = models.BooleanField(default=False)

class CartModel(models.Model):
    product_category = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=100)
    product_price = models.IntegerField(default=0)
    product_image = models.ImageField(default='default.jpeg', upload_to='uploads')
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(default=0)
    host = models.ForeignKey(User, on_delete=models.CASCADE)