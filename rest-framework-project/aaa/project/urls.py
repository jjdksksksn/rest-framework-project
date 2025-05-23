"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(openapi.Info(
    title='Api',
    description="Loyiha uchun documentation",
    default_version='5.1',
    terms_of_service="https://policies.google.com/terms",
    contact=openapi.Contact(email='eqoyirov@gmail.com'),
    license=openapi.License(name="API")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,), 
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projectapp.urls')),
    path('dj-rest-auth/',include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('allauth/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc-ui'),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
