from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]
