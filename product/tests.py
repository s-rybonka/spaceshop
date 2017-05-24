from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from django.core.management import call_command
from test_plus import TestCase as TestCasePlus
from django.utils import timezone

from product.models import Category, Product
from accounts.models import Account


class CategoryTestCase(TestCase):
    '''TestCase for Category'''

    def setUp(self):
        ''' Load data for testing from fixtures (categories_data) here

        :return: object_list
        '''
        call_command('loaddata', 'categories_data', verbosity=0)
        self.client = Client()

    def test_categories_valid_description(self):
        laptop = Category.objects.get(name='Laptops')
        phones = Category.objects.get(name='Phones')
        self.assertTrue(laptop.get_short_description())
        self.assertTrue(phones.get_short_description())

    def test_categories_amount(self):
        categories_list = Category.objects.count()
        self.assertEquals(10, categories_list)

    def test_categories_data_correct(self):
        ''' Check category amount per page,
        check template is loaded

        :return: category objects
        '''
        response = self.client.get(reverse('categories'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/category_list.html')
        self.assertEquals(len(response.context['object_list']), 5)


class ProductTestCase(TestCasePlus):
    '''TestCase for Product'''

    def setUp(self):
        '''
        Load test data from fixtures (categories_data, products_data),
        Create several (desk, pen, mouse), objects, created at real time
        for testing latest products page

        :return: categories and products objects
        '''
        call_command('loaddata', 'categories_data', 'products_data', verbosity=0)
        desk = Product(name='Desk', price='100', slug='desk-3243', category_id=1, description='Good desk',
                       created_at=timezone.now())
        pen = Product(name='Pen', price='100', slug='pen-3243', category_id=1, description='Good pen',
                      created_at=timezone.now())
        mouse = Product(name='Mouse', price='100', slug='mouse-3243', category_id=1, description='Good mouse',
                        created_at=timezone.now())
        Product.objects.bulk_create([desk, pen, mouse])
        self.client = Client()

    def test_categories_amount(self):
        categories_list = Product.objects.count()
        self.assertEquals(48, categories_list)

    def test_products_data_correct(self):
        ''' Cheack products page valid

        :return: categories
        '''
        category = Category.objects.first()
        response = self.client.get(reverse('products', kwargs={'category_slug': category.slug}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_in_category_list.html')
        self.assertEquals(len(response.context['object_list']), 5)

    def test_product_details_data(self):
        ''' Check products details page

        :return: single object
        '''
        category = Category.objects.get(pk=1)
        product = Product.objects.filter(category=1).first()
        response = self.client.get(
            reverse('product_details', kwargs={'category_slug': category.slug, 'product_slug': product.slug}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_details_page.html')
        self.assertTrue(response.context['object'])

    def test_all_products_data(self):
        ''' Check all products page

        :return: object_list
        '''
        response = self.client.get(reverse('all_products'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_list.html')
        self.assertEquals(len(response.context['object_list']), 10)

    def test_latest_products(self):
        '''
        Check latest products page,
        if view is protected
        '''
        user = Account.objects.create(email='test@test.com')
        user.set_password('12345')
        user.save()

        self.assertLoginRequired('latest_products')

        with self.login(email='test@test.com', password='12345'):
            self.get('latest_products')
            self.assertTrue('object_list')
