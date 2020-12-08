from django.urls import path
from .views import ProductAPIView, ProductDetailsAPIView
from .views import CustomerAPIView, CustomerDetailsAPIView  

urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('products/<int:id>/', ProductDetailsAPIView.as_view()),

    path('customers/', CustomerAPIView.as_view()),
    path('customers/<int:id>/', CustomerDetailsAPIView.as_view())
]