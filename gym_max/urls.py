"""gym_max URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import login_page, register_page, guest_register_view
from .views import home_page, about
from products.views import product_list, product_detail
from django.views.static import serve
from cart.views import cart_home
from .settings import MEDIA_ROOT
from django.contrib.auth.views import LogoutView
from addresses.views import checkout_address_create_view
from contact import urls as urls_contact
from search import urls as urls_search
from blog import views
from search import views
from . import views
from billing.views import payment_method_view, payment_method_createview


urlpatterns = [
    url(r'^$', home_page, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^blog/', include('blog.urls')),
    url(r'^contact/', include(urls_contact)),
    url(r'^search/', include('search.urls')),
    url(r'^login/$', login_page, name="login"),
    url(r'^checkout/address/create/$',
        checkout_address_create_view,
        name="checkout_address_create"),
    url(r'^register/guest/$', guest_register_view, name="guest_register"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^cart/', include("cart.urls", namespace="cart")),
    url(r'^billing/payment-method/$',
        payment_method_view,
        name="billing-payment-method"),
    url(r'^billing/payment-method/create/$',
        payment_method_createview,
        name='billing-payment-method-endpoint'),
    url(r'^register/$', register_page, name="register"),
    url(r'^products/$', product_list, name="products"),
    url(r'^products/(?P<pk>\d+)/$', product_detail, name="product_detail"),
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': MEDIA_ROOT
    }),
    url(r'^admin/', admin.site.urls),

]


