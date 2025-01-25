
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('apps.urls')),
       path('api-auth/', include('rest_framework.urls')),
       path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
       path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
