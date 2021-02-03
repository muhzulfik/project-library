from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('profil/', include('profil.urls')),
    path('petunjuk/', include('petunjuk.urls')),
    path('layanan/', include('layanan.urls')),
    path('crud/', include('crudPage.urls')),
    path('staff/', include('pagestaff.urls')),
]
