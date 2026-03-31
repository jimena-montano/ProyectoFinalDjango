from rest_framework import serializers
from .models import Restaurante, Producto, Repartidor, Pedido

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class RepartidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repartidor
        fields = '__all__'