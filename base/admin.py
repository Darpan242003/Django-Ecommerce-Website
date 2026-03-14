from django.contrib import admin
from base.models import ProductsModel, CategoryModel, CartModel

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display=['product_category', 'product_name', 'product_desc', 'product_price', 'product_image']

admin.site.register(ProductsModel, ProductsAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name']

admin.site.register(CategoryModel, CategoryAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=['product_name', 'product_desc', 'product_price']

admin.site.register(CartModel, CartAdmin)
