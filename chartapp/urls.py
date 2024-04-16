from django.urls import path
from . import views
from django.contrib.auth import views as auth_views





urlpatterns = [

    
    path('register/', views.register, name="register"),
    path('login/', views.my_login, name="login"),
    path('user-logout', views.user_logout, name="user-logout"),
    path('home/', views.home, name="home"),
    path('op', views.op, name="op"),
    path('sales', views.sales, name="sales"),
    path('finance', views.finance, name="finance"),
    path('calendar',views.calendar,name="calendar"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),


    #path('chat', views.chat, name="chat"),
    #path('enterchat', views.enterchat, name='enterchat'),
    #path('<str:room>/', views.room, name='room'),
    #path('checkview', views.checkview, name='checkview'),
    #path('send', views.send, name='send'),
    #path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('', views.index, name='index'),



]
