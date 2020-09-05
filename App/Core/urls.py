from django.urls import path, include
from rest_framework import routers


router = routers.DefaultRouter()

# Receituario Endpoint API
#router.register(
#    r'receituarios',
#    ReceituarioViewset,
#    basename='receituarios'
#)