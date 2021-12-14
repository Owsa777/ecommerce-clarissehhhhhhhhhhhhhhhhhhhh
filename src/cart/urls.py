from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name = 'sumary'),
    path('shop/', views.ProductListView.as_view(), name = 'product-list'),
    path('shop/<slug>/', views.ProductDetailView.as_view(), name = 'product-detail'),
    path('increase-quantity/<pk>/', views.IncreaseQuantity.as_view(), name = 'increase-quantity'),
    path('decreace-quantity/<pk>/', views.DecreaceQuantity.as_view(), name = 'decreace-quantity')
]
