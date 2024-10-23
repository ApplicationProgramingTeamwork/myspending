from django.urls import path
from render import views

app_name = 'render'

urlpatterns = [
    path('', views.home, name='home'),
    path('receipts/', views.receipt_list, name='receipts'), 
    path('products/', views.product_list, name='products'),  
    path('receipts/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'), 
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),  
    path('new_receipt/', views.new_receipt, name='new_receipt'),
    path('new_product/', views.new_product, name='new_product'),
    path('edit_receipt/<int:receipt_id>/', views.edit_receipt,name='edit_receipt'),
    path('edit_product/<int:product_id>/', views.edit_product,name='edit_product'),
]

