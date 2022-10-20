from django.shortcuts import render
from .models import Product, Category
from rest_framework import generics
from rest_framework.views import APIView, Response
from .serializers import CreateProductSerializer


# class ProductCreateView(APIView):
#
#     def post(self, request):
#         product = CreateProductSerializer(data=request.data)
#         if product.is_valid():
#             product.save()
#         return Response(status=201)


class ProductView(APIView):

