from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("users.urls")),
    path('', include("library.urls")),
    path("", include("student.urls")),
    path("", include("course.urls")),
    path("", include("blog.urls")),
    path('', HomePage.as_view(), name="university")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)