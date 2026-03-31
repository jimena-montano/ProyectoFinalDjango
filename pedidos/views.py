from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurante, Producto, Repartidor
from .serializers import RestauranteSerializer, ProductoSerializer, RepartidorSerializer

# Los 3 ModelViewSets (CRUD automático)
class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class RepartidorViewSet(viewsets.ModelViewSet):
    queryset = Repartidor.objects.all()
    serializer_class = RepartidorSerializer

# 1 Custom API (Lógica manual)
class StatusAPIView(APIView):
    def get(self, request):
        return Response({"mensaje": "Servidor de Delivery Operativo", "version": "1.0"})
