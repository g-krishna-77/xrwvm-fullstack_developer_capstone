"""
djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/

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
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    path('djangoapp/', include('djangoapp.urls')),
    
    # Home and static HTML pages
    path('', TemplateView.as_view(template_name="Home.html"), name='home'),
    path('about/', TemplateView.as_view(template_name="About.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="Contact.html"), name='contact'),
    
    # Authentication pages (React)
    path('login/', TemplateView.as_view(template_name="index.html"), name='login'),
    path('register/', TemplateView.as_view(template_name="index.html"), name='register'),
    
    # Dealers pages (React)
    path('dealers/', TemplateView.as_view(template_name="index.html"), name='dealers'),
    path('dealer/<int:dealer_id>/', TemplateView.as_view(template_name="index.html"), name='dealer_details'),
    path('postreview/<int:dealer_id>/', TemplateView.as_view(template_name="index.html"), name='postreview'),
    
    # Serve React manifest and meta files from build directory
    path('manifest.json', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend', 'build'),
        'path': 'manifest.json'
    }),
    path('favicon.ico', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend', 'build'),
        'path': 'favicon.ico'
    }),
    path('robots.txt', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend', 'build'),
        'path': 'robots.txt'
    }),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
