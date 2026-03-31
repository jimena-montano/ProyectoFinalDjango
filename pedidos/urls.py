from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestauranteViewSet, ProductoViewSet, RepartidorViewSet, StatusAPIView

# El router se encarga de las rutas automáticas (ModelViewSets)
router = DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'repartidores', RepartidorViewSet)

urlpatterns = [
    # Rutas del Router
    path('', include(router.urls)),
    
    # Requisito: Al menos 1 Custom API
    path('status/', StatusAPIView.as_view(), name='api-status'),
]