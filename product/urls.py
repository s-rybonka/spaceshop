from django.conf.urls import url

from product import views as product_views

urlpatterns = [
    url(r'^$',
        product_views.CategoryView.as_view(),
        name='categories'),
    url(r'^all-products/$',
        product_views.AllProductsViews.as_view(),
        name='all_products'),
    url(r'^products/(?P<category_slug>\w+-\d+)/$',
        product_views.ProductsView.as_view(),
        name='products'),
    url(r'^products/(?P<category_slug>\w+.*\d+)/(?P<product_slug>\w+.*\d+)/$',
        product_views.ProductDetailsViews.as_view(),
        name='product_details'),
    url(r'^latest-products/$',
        product_views.LatestProductsView.as_view(),
        name='latest_products'),
]
