from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('materias_primas/', include('materias_primas.urls')),
    path('', include('produccion.urls')),
    path('admin/', admin.site.urls),
    path('login/', RedirectView.as_view(url=reverse_lazy('login'), permanent=False)),
    path('', include('usuarios.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    path('proveedores/', include('proveedores.urls')),
    path('envasados/', include('envasado.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)