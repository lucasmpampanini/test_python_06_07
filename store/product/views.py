from rest_framework import viewsets, status
from .models import Product
from .serializers import ProductSerializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ProductSerializers
    queryset = Product.objects.all()
