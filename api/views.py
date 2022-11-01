from .models import Product, Category
from rest_framework.views import Response
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAdminOrReadOnly

# class ProductCreateView(APIView):
#
#     def post(self, request):
#         product = CreateProductSerializer(data=request.data)
#         if product.is_valid():
#             product.save()
#         return Response(status=201)


# class ProductAPIView(APIView):
#
#     def get_object(self, pk):
#         try:
#             return Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         product = self.get_object(pk)
#         return Response(model_to_dict(product))
#
#     def post(self, request):
#         product = Product.objects.create(
#             title=request.data.get('title'),
#             price=request.data.get('price')
#         )
#         return Response({'text': model_to_dict(product)})
#
#     def put(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         product.title = request.data.get('title')
#         product.price = request.data.get('price')
#         product.save()
#         return Response({'text': model_to_dict(product)})
#
#     def patch(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         if request.data.get('title'):
#             product.title = request.data.get('title')
#         else:
#             product.price = request.data.get('price')
#         product.save()
#         return Response({'text': model_to_dict(product)})
#
#     def delete(self, request, pk):
#         product = Product.objects.get(pk=pk)
#         product.delete()
#         return Response({'text': 'object deleted'})


# class ProductCreateAPIView(generics.CreateAPIView):
#     def post(self, request):
#         serializer = CreateProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#
# class ProductRetrieveAPIView(generics.RetrieveAPIView):
#     # def get_object(self, pk):
#     #     try:
#     #         return Product.objects.get(pk=pk)
#     #     except Product.DoesNotExist:
#     #         raise Http404
#
#     def get(self, request, pk):
#         serializer = RetrieveProductSerializer(get_object_or_404(Product, pk=pk))
#         return Response(serializer.data)
#
#
# class ProductUpdateAPIView(generics.UpdateAPIView):
#     def put(self, request, *args, **kwargs):
#         prod = get_object_or_404(Product, pk=kwargs.get('pk'))
#         serializer = RetrieveProductSerializer(instance=prod, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#     # def patch(self, request, *args, **kwargs):
#     #     prod = get_object_or_404(Product, pk=kwargs.get('pk'))
#     #     serializer = RetrieveProductSerializer(instance=prod, data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #     return Response(serializer.data)
#
#
# class ProductListAPIView(generics.ListCreateAPIView):
#     # def get(self, request):
#     #     prod = Product.objects.all()
#     #     serializer = RetrieveProductSerializer(prod, many=True)
#     #     return Response(serializer.data)
#     #
#     serializer_class = RetrieveProductSerializer
#     queryset = Product.objects.all()
#     # def post(self, request, *args, **kwargs):
#     #     serializer = CreateProductSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #     return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )

    @action(detail=False, methods=['get'])
    def get_json_text(self, request):
        return Response({'text': '123'})

    @action(detail=False, methods=['get'])
    def get_categorys(self, request):
        categs = Category.objects.all()
        serializer = CategorySerializer(categs, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


