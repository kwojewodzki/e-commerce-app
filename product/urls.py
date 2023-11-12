from django.urls import path
from product import views

urlpatterns = [
    path('', views.ListProductsAPIView.as_view(), name='list_products'),
    path('<int:pk>/', views.DetailProductAPIView.as_view(), name="retrieve_product"),
    path('create/', views.CreateProductAPIView.as_view()),
    path('modify/<int:pk>/', views.UpdateDeleteProductAPIView.as_view()),
    path('statistics/', views.GetStatisticsAPIView.as_view())
]
