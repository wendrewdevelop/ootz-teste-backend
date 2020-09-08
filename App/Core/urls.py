from django.urls import path, include
from rest_framework import routers
from App.Produto.api.viewsets import ProdutoViewset
from App.Kit.api.viewsets import KitViewset


router = routers.DefaultRouter()

# Produto Endpoint API
router.register(
    r'produtos',
    ProdutoViewset,
    basename='produtos'
)

# Kit Produto Endpoint API
router.register(
    r'kit_produtos',
    KitViewset,
    basename='kit_produtos'
)