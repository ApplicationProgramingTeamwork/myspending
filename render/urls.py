from django.urls import path
from render import views

app_name = 'render'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='products'),  
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),  
    path('products/<int:product_id>/edit_product/', views.edit_product, name='edit_product'),
    path('receipts/', views.receipt_list, name='receipts'), 
    path('receipts/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'), 
    path('receipts/<int:receipt_id>/edit_receipt/', views.edit_receipt, name='edit_receipt'),
    path('receipts/<int:receipt_id>/delete_receipt/', views.delete_receipt, name='delete_receipt'),
    path('receipts/<int:receipt_id>/new_product/', views.new_product, name='new_product'),
    path('receipts/new_receipt/', views.new_receipt, name='new_receipt'),
]
