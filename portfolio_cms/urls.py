from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView 

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('api/', include('api.urls')),  # Include the URLs from your api app
    path('api/auth/', include('djoser.urls')),  # Djoser auth endpoints
    path('api/auth/', include('djoser.urls.jwt')),  # JWT authentication with Djoser
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # ReDoc UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

