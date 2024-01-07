from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name="register"),
    path('login', views.my_login, name="login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('home/', views.home, name="home"),
    path('op', views.op, name="op"),
    path('sales', views.sales, name="sales"),
    path('finance', views.finance, name="finance"),
    path('chat', views.chat, name="chat"),
    path('enterchat', views.enterchat, name='enterchat'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),

]
