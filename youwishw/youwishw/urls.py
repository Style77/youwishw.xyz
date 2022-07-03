from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    # path('music/', include('music.urls')),
    path('', include('music.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
