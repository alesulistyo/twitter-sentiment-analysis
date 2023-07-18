from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('tweets/', include('tweets.urls')),
    path('preprocessing/', include('preprocessing.urls')),
    path('processing/', include('processing.urls')),
    path('validation/', include('validation.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
