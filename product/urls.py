from django.urls import path
from order import views

urlpatterns = [
    path('products/', views.ListProductsAPIView.as_view(), name='list_products'),
    path('products/<int:pk>/', views.DetailProductAPIView.as_view(), name="retrieve_product"),
    path('products/create/', views.CreateProductAPIView.as_view()),
    path('products/modify/<int:pk>/', views.UpdateDeleteProductAPIView.as_view())
]
