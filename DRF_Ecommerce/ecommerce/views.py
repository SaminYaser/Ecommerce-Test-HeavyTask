from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Customer
from .serializers import ProductSerializer, CustomerSerializer

class BoilerClass (APIView):
    """
    A boiler class to handle bulk get and post methods for models.
    """

    def __init__(self, model, serializer, fields=None):
        # Pass fields list to choose keys for get method
        self.boilerModel = model
        self.boilerSerializer = serializer
        self.bulkGetFields = fields

    def get(self, request):
        instances = self.boilerModel.objects.all()
        serializer = self.boilerSerializer(instances, many=True, fields=self.bulkGetFields)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.boilerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class BoilerClassForIndividuals (APIView):
    """
    A boiler class to handle get, put, patch, delete methods for models.
    """

    def __init__(self, model, serializer):
        self.boilerModel = model
        self.boilerSerializer = serializer
    
    def get_object(self, id):
        # Function to retrieve data from database
        try:
            return self.boilerModel.objects.get(id=id)
        except self.boilerModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        instance = self.get_object(id)
        serializer = self.boilerSerializer(instance)
        return Response(serializer.data)
    
    def put(self, request, id):
        instance = self.get_object(id)
        serializer = self.boilerSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
    def patch(self, request, id):
        instance = self.get_object(id)
        serializer = self.boilerSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Product Views classes
## /products/
class ProductAPIView (BoilerClass):
    
    def __init__(self):
        super().__init__(model=Product, serializer=ProductSerializer, fields=[
            'id',
            'name', 
            'price',
            'is_discounted', 
            'discounted_price', 
            'thumbnail'
        ])
## /products/:id        
class ProductDetailsAPIView (BoilerClassForIndividuals):
    def __init__(self):
        super().__init__(model=Product, serializer=ProductSerializer)
    


# Customer Views classes
## /customers/
class CustomerAPIView (BoilerClass):

    def __init__(self):
        super().__init__(model=Customer, serializer=CustomerSerializer, fields=[
            'id',
            'name', 
            'email',
            'mobile_number', 
            'profile_picture'
        ])
## /customers/:id/
class CustomerDetailsAPIView (APIView):
    def __init__(self):
        super().__init__(model=Customer, serializer=CustomerSerializer)