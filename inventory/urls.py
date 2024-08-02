from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('inventory/add/', views.add_item, name='add_item'),
    path('inventory/<int:pk>/edit/', views.update_item, name='update_item'),
    path('inventory/<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('ingredients/', views.ingredient_list, name='ingredient_list'),
    path('ingredients/add/', views.add_ingredient, name='add_ingredient'),
    path('ingredients/<int:pk>/edit/', views.update_ingredient, name='update_ingredient'),
    path('ingredients/<int:pk>/delete/', views.delete_ingredient, name='delete_ingredient'),
    path('orders/', views.order_list, name='order_list'),
    path('orders/<int:pk>/', views.order_detail, name='order_detail'),
    path('orders/add/', views.add_order, name='add_order'),
    path('sales/', views.sales_list, name='sales_list'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
