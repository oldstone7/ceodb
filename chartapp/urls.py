from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import FinanceViewSet
from django.urls import include
from .views import *

router = DefaultRouter()
router.register(r'finance', FinanceViewSet, basename='finance')
router.register(r'otp', OTPViewSet, basename='otp')
router.register(r'product', ProductViewSet)
router.register(r'metrics', MetricsViewSet)
router.register(r'leadconversion', LeadConversionRateViewSet)
router.register(r'supplychain', SupplyChainViewSet)
router.register(r'inventory', InventoryViewSet)
router.register(r'production', ProductionOutputViewSet)
router.register(r'efficiency', EfficiencyViewSet)
router.register(r'salesfigure', SalesFigureViewSet)



urlpatterns = [

    path('register/', views.register, name="register"),
    path('login/', views.my_login, name="login"),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('logout/', views.user_logout, name="logout"),
    path('not-authorized/', not_authorized, name='not_authorized'),
    path('op', views.op, name="op"),
    path('sales', views.sales, name="sales"),
    path('finance', views.finance, name="finance"),
    path('admindash/',views.admindash,name="admindash"),
    
    path('api/', include(router.urls)),
    path('api/user_info/', user_info, name='user_info'),
    path('api/sales', sales_api, name='sales_api'),

    # Admin User URLs
    path('admindash/users/', views.admin_user_list, name='admin_user_list'),
    path('admindash/users/create', views.admin_user_create, name='admin_user_create'),
    path('admindash/users/<int:user_id>/', views.admin_user_detail, name='admin_user_detail'),
    path('admindash/users/<int:user_id>/edit/', views.admin_user_update, name='admin_user_update'),
    path('admindash/users/<int:user_id>/delete/', views.admin_user_delete, name='admin_user_delete'),
    path('admindash/users/<int:user_id>/change_password/', views.admin_user_change_password, name='admin_user_change_password'),

    # Admin Product URLs
    path('admindash/products/', views.product_list, name='product_list'),
    path('admindash/products/create/', views.product_create, name='product_create'),
    path('admindash/products/<int:product_id>/edit/', views.product_update, name='product_update'),
    path('admindash/products/<int:product_id>/delete/', views.product_delete, name='product_delete'),

    # Admin Finance URLs
    path('admindash/finance/', finance_list, name='finance_list'),
    path('admindash/finance/create/', finance_create, name='finance_create'),
    path('admindash/finance/<int:finance_id>/edit/', finance_update, name='finance_update'),
    path('admindash/finance/<int:finance_id>/delete/', finance_delete, name='finance_delete'),

    # Password Reset
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    path('', views.index, name='index'),


]
