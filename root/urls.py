from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
