from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('shop/', include('store.urls')),
    path('carrito/', include('carrito.urls')),
    path('pago_cancelado/', include('carrito.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
