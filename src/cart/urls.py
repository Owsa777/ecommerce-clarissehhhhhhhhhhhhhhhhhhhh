from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name = 'sumary'),
    path('shop/', views.ProductListView.as_view(), name = 'product-list'),
    path('shop/<slug>/', views.ProductDetailView.as_view(), name = 'product-detail'),
    path('increase-quantity/<pk>/', views.IncreaseQuantity.as_view(), name = 'increase-quantity'),
    path('decrease-quantity/<pk>/', views.DecreaseQuantity.as_view(), name = 'decrease-quantity'),
    path('delete-product/<pk>/', views.DeleteProduct.as_view(), name = 'delete-product'),
    path('checkout/', views.CheckoutView.as_view(), name = 'checkout')
]
