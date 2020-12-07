from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer

# Create your views here.

class ProductAPIView (APIView):
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, fields=[
            'id',
            'name', 
            'price',
            'is_discounted', 
            'discounted_price', 
            'thumbnail'
        ])
        return Response(serializer.data)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailsAPIView (APIView):

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def patch(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)