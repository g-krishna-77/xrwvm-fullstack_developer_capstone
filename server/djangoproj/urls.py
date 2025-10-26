"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
    path('', TemplateView.as_view(
        template_name="Home.html"), name='home'),
    path('about/', TemplateView.as_view(
        template_name="About.html"), name='about'),
    path('contact/', TemplateView.as_view(
        template_name="Contact.html"), name='contact'),

    # Authentication pages (React)
    path('login/', TemplateView.as_view(
        template_name="index.html"), name='login'),
    path('register/', TemplateView.as_view(
        template_name="index.html"), name='register'),

    # Dealers pages (React)
    path('dealers/', TemplateView.as_view(
        template_name="index.html"), name='dealers'),
    path('dealer/<int:dealer_id>/', TemplateView.as_view(
        template_name="index.html"), name='dealer_details'),
    path('postreview/<int:dealer_id>/', TemplateView.as_view(
        template_name="index.html"), name='postreview'),

    # Serve React manifest and meta files
    path('manifest.json', serve, {
        'document_root': os.path.join(
            settings.BASE_DIR, 'frontend', 'build'
        ),
        'path': 'manifest.json'
    }),
    path('favicon.ico', serve, {
        'document_root': os.path.join(
            settings.BASE_DIR, 'frontend', 'build'
        ),
        'path': 'favicon.ico'
    }),
    path('robots.txt', serve, {
        'document_root': os.path.join(
            settings.BASE_DIR, 'frontend', 'build'
        ),
        'path': 'robots.txt'
    }),
    path('logo192.png', serve, {
        'document_root': os.path.join(
            settings.BASE_DIR, 'frontend', 'build'
        ),
        'path': 'logo192.png'
    }),

] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)
