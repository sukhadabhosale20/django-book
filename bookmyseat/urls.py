"""from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('',include('users.urls')),
    path('movies/', include('movies.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views  # Import views for the 'About' and 'Contact' pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # User-related URLs
    path('', include('users.urls')),       # Default homepage routing (if handled by 'users' app)
    path('movies/', include('movies.urls')),  # Movies-related URLs
    path('about/', views.about, name='about'),  # About Us static page
    path('contact/', views.contact, name='contact'),  # Contact Us static page
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
