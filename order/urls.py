from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListProductsAPIView.as_view(), name='list_products')
]
