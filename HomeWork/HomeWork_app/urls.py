from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.inventory_list, name='inventory_list'),
    path('inventory/replenish/<int:count>/', views.inventory_replenish, name='inventory_replenish'),
    path('inventory/alerts/', views.inventory_alerts, name='inventory_alerts'),
]
