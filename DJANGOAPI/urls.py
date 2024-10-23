"""
URL configuration for DJANGOAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api.login.login_views import (
    login_views, 
    forgot_views,
    register_views,
    logout_views
    )
from api.home.home_views import (
    home_views,
    blog_views,
    cart_views,
    category_views,
    checkout_views,
    confirmation_views,
    contact_views,
    elements_views,
    singleblog_views,
    singleproduct_views,
    tracking_views
    )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_views, name='login'),
    path('logout/', logout_views, name='logout'),
    path('forgot/', forgot_views, name='forgot'),
    path('register/', login_views, name='register'),
    path('', home_views, name='home'),
    path('home/', home_views, name='home'),
    path('blog/', blog_views, name='blog'),
    path('cart/', cart_views, name='cart'),
    path('category/', category_views, name='category'),
    path('checkout/', checkout_views, name='checkout'),
    path('confirmation/', confirmation_views, name='confirmation'),
    path('contact/', contact_views, name='contact'),
    path('elements/', elements_views, name='elements'),
    path('single-blog/', singleblog_views, name='single-blog'),
    path('single-product/', singleproduct_views, name='single-product'),
    path('tracking/', tracking_views, name='tracking'),
    
]
