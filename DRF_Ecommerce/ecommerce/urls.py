from django.urls import path
from .views import ProductAPIView, ProductDetailsAPIView  

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('<int:id>/', ProductDetailsAPIView.as_view())
]