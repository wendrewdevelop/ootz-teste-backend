from django.urls import path, include
from rest_framework import routers
from App.Produto.api.viewsets import ProdutoViewset


router = routers.DefaultRouter()

# Produto Endpoint API
router.register(
    r'produtos',
    ProdutoViewset,
    basename='produtos'
)