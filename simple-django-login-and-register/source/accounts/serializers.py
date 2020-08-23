from rest_framework import serializers
from .models import Activation,Address,Vendor




class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activation
        fields = ('id', 'url', 'user', 'created_at', 'code', 'email')

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'url', 'address', 'city', 'state', 'country')

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'url', 'user', 'phone', 'bio', 'image', 'active', 'address', 'created_at')