from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('users/', include('users.urls', namespace='users')),
    path('api/contacts', include('contacts.api.urls', namespace='api'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
