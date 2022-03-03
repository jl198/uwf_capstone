from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('games/', include('games.urls')),
    # path('upload/', include('upload.urls')),
]
