from django.db import models
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string

from django_resized import ResizedImageField


class Category(models.Model):
    """Category model"""
    name = models.CharField(max_length=30, verbose_name='Category', blank=False, unique=True)
    slug = models.SlugField(max_length=30, verbose_name='Slug', unique=True)
    image = ResizedImageField(size=[320, 300], crop=['middle', 'center'], verbose_name='Image', upload_to='media',
                              blank=True, null=True, quality=100)
    description = models.CharField(max_length=1024, verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """ Get category name

        :return: string
        """
        return self.name

    def get_short_description(self):
        return '{0}...'.format(self.description[:50])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Generate unique slug for each category with (get_random_string()) function,
        slug contains category name and random generated 4 digits

        :param force_insert:
        :param force_update:
        :param using:
        :param update_fields:
        :return: category object
        """

        self.slug = slugify('{0}-{1}'.format(self.name, get_random_string(4, '0123456789')))

        super(Category, self).save()


class Product(models.Model):
    """Product model"""
    category = models.ForeignKey('product.Category', related_name='products', verbose_name='Category', null=True)
    name = models.CharField(verbose_name='Product', max_length=30)
    slug = models.SlugField(max_length=30, verbose_name='Slug', unique=True)
    image = ResizedImageField(size=[240, 240], crop=['middle', 'center'], verbose_name='Image', upload_to='media',
                              null=True, blank=True)
    description = models.CharField(max_length=1024, verbose_name='description')
    price = models.FloatField(verbose_name='Price')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """ Get product name

        :return: string
        """
        return self.name

    def get_products_description(self):
        return '{0}...'.format(self.description[:30])

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Generate unique slug for each product with (get_random_string()) function,
        slug contains product name and random generated 4 digits

        :param force_insert:
        :param force_update:
        :param using:
        :param update_fields:
        :return: product object
        """
        self.slug = slugify('{0}-{1}'.format(self.name, get_random_string(4, '0123456789')))

        super(Product, self).save()
