from django.db import models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from decimal import Decimal

from django_resized import ResizedImageField


class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=30, verbose_name='Category', unique=True)
    slug = models.SlugField(max_length=30, verbose_name='Slug', unique=True)
    image = ResizedImageField(size=[320, 300], crop=['middle', 'center'], verbose_name='Image', upload_to='media',
                              blank=True, null=True, quality=100)
    description = models.CharField(max_length=1000, verbose_name='Description')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_short_description(self):
        return '{0}...'.format(self.description[:50])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Generate unique slug for each category with (get_random_string()) function,
        slug contains category name and random generated 4 digits
        """

        self.slug = slugify('{0}-{1}'.format(self.name, get_random_string(4, '0123456789')))

        super().save(force_insert, force_update, using, update_fields)


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey('product.Category', related_name='products', verbose_name='Category', null=True)
    name = models.CharField(verbose_name='Product', max_length=30)
    slug = models.SlugField(max_length=30, verbose_name='Slug', unique=True)
    image = ResizedImageField(size=[240, 240], crop=['middle', 'center'], verbose_name='Image', upload_to='media',
                              null=True, blank=True)
    description = models.CharField(max_length=1000, verbose_name='description')
    price = models.DecimalField(verbose_name='Price', max_digits=23, decimal_places=8, default=Decimal(0.0))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_products_description(self):
        return '{0}...'.format(self.description[:30])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Generate unique slug for each product with (get_random_string()) function,
        slug contains product name and random generated 4 digits

        """
        self.slug = slugify('{0}-{1}'.format(self.name, get_random_string(4, '0123456789')))

        super().save(force_insert, force_update, using, update_fields)
