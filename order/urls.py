from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListProductsAPIView.as_view(), name='list_products'),
    path('<int:pk>/', views.DetailProductAPIView.as_view(), name="retrieve_product"),
    path('add_product/', views.CreateProductAPIView.as_view())
]
