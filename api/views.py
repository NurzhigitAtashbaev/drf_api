from django.shortcuts import render
from .models import Product
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import CreateProductSerializers
from rest_framework.response import Response


class ProductCreateView(APIView):
    """Creating APIView for product"""

    def post(self, request):
        product = CreateProductSerializers(data=request.data)
        if product.is_valid():
            product.save()
        return Response(status=201)
