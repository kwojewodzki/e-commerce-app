from django.urls import path, register_converter
from product import views
from product.converters import DateConverter

register_converter(DateConverter, 'date')

urlpatterns = [
    path('', views.ListProductsAPIView.as_view(), name='list_products'),
    path('<int:pk>/', views.DetailProductAPIView.as_view(), name="retrieve_product"),
    path('create/', views.CreateProductAPIView.as_view()),
    path('modify/<int:pk>/', views.UpdateDeleteProductAPIView.as_view()),
    path('statistics/<date:start_date>/<date:end_date>/<int:count>', views.GetStatisticsAPIView.as_view())
]
