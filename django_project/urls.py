from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from pages.views import custom_404, custom_500

urlpatterns = [
    path('epms-admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path("projects/", include("projects.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

handler404 = 'pages.views.custom_404'
handler500 = 'pages.views.custom_500'