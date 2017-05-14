from django.conf.urls import url

from accounts import views as custom_auth_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', custom_auth_views.RegisterView.as_view(), name="register"),

    url(r'^login/$', custom_auth_views.LoginView.as_view(), name="login"),

    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name="logout"),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
