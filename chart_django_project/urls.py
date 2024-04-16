from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('password_reset/', include('chartapp.urls')),
    path('', include('chartapp.urls')),
    path('chat/' ,include('chat.urls')),
]
