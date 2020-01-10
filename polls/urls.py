from django.urls import path, include

from polls import views

app_name = 'polls'

urlpatterns = [
    path('products', views.ProductList.as_view(), name='product_list'),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
]
