import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from django.urls import re_path

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.main, name='main'),
    re_path(r'^products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contact, name='contact'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', include('adminapp.urls', namespace='admin')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
