from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('productos/', include('materias_primas.urls')),
    path('', include('produccion.urls')),
    path('admin/', admin.site.urls),
    path('login/', include('usuarios.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)