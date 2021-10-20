from django.contrib import admin
from django.urls import path, include, re_path
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contact, name='contact'),
    path('', mainapp.main, name='main'),
    path('auth/',  include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('', include('social_django.urls', namespace='social')),
    re_path(r'^order/', include('ordersapp.urls', namespace='order')),
]

if settings.DEBUG:
   import debug_toolbar

   urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
