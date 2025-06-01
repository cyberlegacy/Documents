from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('japanese_class_app.urls')), # Include app-level URLs
]
