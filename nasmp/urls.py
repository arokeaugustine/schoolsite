from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staffpage.urls')),
    path('gallery/', include('gallery.urls')),
    path('wing/', include('wing.urls')),
    # path('contact/', include('contact.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "OFFICIALLY NASMP"
admin.site.site_title = "NASMP Admin"
admin.site.index_title = "Welcome To The Admin Dashboard"

