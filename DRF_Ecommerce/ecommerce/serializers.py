from rest_framework import serializers
from .models import Product, Customer, Order

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class ProductSerializer (DynamicFieldsModelSerializer):
    gallery = serializers.ListField(child=serializers.CharField(max_length=1000))
    available_colours = serializers.ListField(child=serializers.CharField(max_length=1000))
    available_sizes = serializers.ListField(child=serializers.CharField(max_length=1000))
    
    class Meta:
        model = Product
        fields = [
            'id',
            'name', 
            'price',
            'is_discounted', 
            'discounted_price', 
            'thumbnail', 
            'gallery', 
            'rating', 
            'available_colours', 
            'available_sizes', 
            'description'
        ]

class CustomerSerializer (DynamicFieldsModelSerializer):
    saved_addresses = serializers.ListField(child=serializers.JSONField())

    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'email',
            'mobile_number',
            'profile_picture',
            'permanent_address',
            'saved_addresses'
        ]

class OrderSerializer (DynamicFieldsModelSerializer):

    class Meta:
        model = Order
        fields = [
            'customer_id',
            'total_price',
            'delivery_status',
            'refund_status',
            'date',
            'product_list',
            'billing_address',
            'shipping_address'
        ]