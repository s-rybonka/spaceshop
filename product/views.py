from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from .models import Category, Product


class CategoryView(ListView):
    template_name = 'product/category.html'

    def get_queryset(self):
        return Category.objects.all()


class AllProductsViews(ListView):
    template_name = 'product/all_products.html'
    model = Product


class ProductsView(ListView):
    template_name = 'product/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data()

        category_slug = self.kwargs.get('category_slug')

        context['category_slug'] = category_slug[:-5]

        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get('category_slug'))


class ProductDetailsViews(DetailView):
    template_name = 'product/product_details.html'
    model = Product

    def get_object(self, queryset=None):
        return Product.objects.get(slug=self.kwargs.get('product_slug'))


class LatestProductsView(LoginRequiredMixin, ListView):
    template_name = 'product/latest_products.html'
    hours_24 = timezone.now() - timezone.timedelta(days=1)

    def get_queryset(self):
        hours_24 = timezone.now() - timezone.timedelta(days=1)
        return Product.objects.filter(created_at__gte=hours_24)
