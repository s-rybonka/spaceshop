from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Category', blank=False, unique=True)
    slug = models.SlugField(max_length=30,verbose_name='Slug', unique=True)
    description = models.CharField(max_length=1024, verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.id)
        super(Category, self).save()


class Product(models.Model):
    name = models.CharField(verbose_name='Product',max_length=30)
    slug = models.ForeignKey('product.Category',related_name='products',verbose_name='Category')
    description = models.CharField(max_length=1024, verbose_name='description')
    price = models.FloatField(verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    modified_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return str(self.name)


