from django.contrib import admin
from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description',)


class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'description', 'price',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
