# image_upload_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.image_upload, name='image_upload'),
    path('images/', views.image_list, name='image_list'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)