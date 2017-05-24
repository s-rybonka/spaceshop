from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin

# Own modules
from .models import Category, Product


class CategoryView(SuccessMessageMixin, ListView):
    paginate_by = 5
    template_name = 'product/category_list.html'

    def get_queryset(self):
        return Category.objects.all()


class AllProductsViews(ListView):
    paginate_by = 10
    template_name = 'product/product_list.html'
    model = Product


class ProductsView(ListView):
    paginate_by = 5
    template_name = 'product/product_in_category_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data()

        category_slug = self.kwargs.get('category_slug')

        context['category_slug'] = category_slug

        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get('category_slug'))


class ProductDetailsViews(DetailView):
    template_name = 'product/product_details_page.html'
    model = Product

    def get_object(self, queryset=None):
        return Product.objects.get(slug=self.kwargs.get('product_slug'))


class LatestProductsView(LoginRequiredMixin, ListView):
    paginate_by = 5
    template_name = 'product/latest_product_list.html'

    def get_queryset(self):
        time_24_hours_ago = timezone.now() - timezone.timedelta(days=1)

        return Product.objects.filter(created_at__gte=time_24_hours_ago)
