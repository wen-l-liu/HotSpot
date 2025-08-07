from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path(
        '<slug:slug>/edit_review/<int:review_id>',
        views.review_edit, name='review_edit'),
    path(
        '<slug:slug>/delete_review/<int:review_id>',
        views.review_delete, name='review_delete'),
]
