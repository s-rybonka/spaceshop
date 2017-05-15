from django.contrib import admin
from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description','image',)


class ProductAdmin(admin.ModelAdmin):
    fields = ('name',  'description', 'price','category','image',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
