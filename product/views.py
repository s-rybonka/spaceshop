from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin

# Own modules
from .models import Category, Product


class CategoryView(SuccessMessageMixin, ListView):
    '''
    Get all categories 5 per page here
    '''
    paginate_by = 5
    template_name = 'product/categories.html'

    def get_queryset(self):
        return Category.objects.all()


class AllProductsViews(ListView):
    '''Get all products, 10 per page'''
    paginate_by = 10
    template_name = 'product/all_products.html'
    model = Product


class ProductsView(ListView):
    '''Get some products inside chosen category
    5 per page
    '''
    paginate_by = 5
    template_name = 'product/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data()

        # get slug from kwargs
        category_slug = self.kwargs.get('category_slug')

        # set slug to context
        context['category_slug'] = category_slug

        return context

    def get_queryset(self):
        '''Get products

        :return: object_list depend on category_slug
        '''
        return Product.objects.filter(category__slug=self.kwargs.get('category_slug'))


class ProductDetailsViews(DetailView):
    '''
    Get single product here
    '''
    template_name = 'product/product_details.html'
    model = Product

    def get_object(self, queryset=None):
        '''

        :param queryset:
        :return: object depend on slug
        '''
        return Product.objects.get(slug=self.kwargs.get('product_slug'))


class LatestProductsView(LoginRequiredMixin, ListView):
    '''
    Get latest products list in 24 hours
    '''
    paginate_by = 5
    template_name = 'product/latest_products.html'
    hours_24 = timezone.now() - timezone.timedelta(days=1)

    def get_queryset(self):
        ''' Get products list which added during 24 hours

        :return: queryset
        '''
        hours_24 = timezone.now() - timezone.timedelta(days=1)
        return Product.objects.filter(created_at__gte=hours_24)
