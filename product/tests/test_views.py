from django.test import TestCase
from django.core.urlresolvers import reverse


class CategoryViewTest(TestCase):
    def test_categories_page(self):
        response = self.client.get(reverse('categories'))
        self.assertEquals(response.status_code, 200)


class AllProductsViewsTest(TestCase):
    def test_all_products_page(self):
        response = self.client.get(reverse('all_products'))
        self.assertEquals(response.status_code, 200)


class ProductsViewTest(TestCase):
    def test_products_page(self):
        response = self.client.get(reverse('products', kwargs={'category_slug': 'sport-1232'}))
        self.assertEquals(response.status_code, 200)

from product.models import Product
class ProductDetailsViewsTest(TestCase):
    def test_product_detail_page(self):
        product = Product.objects.create(name='Phone',description='Description',slug='phone-good-1234',price=12)
        product.save()
        response = self.client.get(
            reverse('product_details', kwargs={'category_slug': 'sport-ware-1232','product_slug': product.slug}))
        self.assertEquals(response.status_code, 200)

# class LatestProductsViewTest(TestCase):
#     def test_latest_products_page(self):
#         response = self.client.get(reverse('latest_products'))
#         self.assertEquals(response.status_code, 200)
