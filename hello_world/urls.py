from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views



urlpatterns = [

             path('', views.index, name='index'),
             path('pasha', views.pasha, name='pasha'),

             # positional read and writes of a pawn
             path('read', views.read, name='read'),
             path('write', views.write, name='write'),

             # splendor reads ans writes
             path('splendor/read', views.pasha, name='splendorread'),
             path('splendor/write', views.splendor_write, name='splendorwrite'),

             ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
