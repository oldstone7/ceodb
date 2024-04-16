from django.urls import path
from . import views
urlpatterns = [
    path('', views.messages_page),
    path('upload_file/', views.upload_file, name='upload_file'),
]
