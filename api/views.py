from django.shortcuts import get_object_or_404
from .models import Product
from django.urls import reverse
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CreateProductSerializer, ProductSerializer


# class ProductCreateView(APIView):
#     """Creating APIView for product"""
#
#     def post(self, request):
#         product = CreateProductSerializer(data=request.data)
#         if product.is_valid():
#             product.save()
#         return Response(status=201)

# class ProductAPIView(APIView):
#     # get, post, put, patch, delete
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
#         product = self.get_object(pk)
#         product.title = request.data.get('title')
#         product.price = request.data.get('price')
#         product.save()
#         return Response({'text': model_to_dict(product)})
#
#     def patch(self, request, pk):
#         product = self.get_object(pk)
#         if request.data.get('title'):
#             product.title = request.data.get('title')
#         else:
#             product.price = request.data.get('price')
#         product.save()
#         return Response({'text': model_to_dict(product)})
#
#     def delete(self, request, pk):
#         product = self.get_object(pk)
#         product.delete()
#         return Response({'text': 'object deleted'})


# class ProductCreateAPIView(generics.CreateAPIView):
#     """CreateAPIView for creating Product objects """
#
#     def post(self, request):
#         serializer = CreateProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#
# class ProductDetailView(generics.RetrieveAPIView):
#     """ Doc. info"""
#
#     def get(self, request, pk):
#         serializer = ProductSerializer(get_object_or_404(Product, pk=pk))
#
#         return Response(serializer.data)
#
#
# class UpdateProductView(generics.UpdateAPIView):
#     def put(self, request, *args, **kwargs):
#         product = get_object_or_404(Product, pk=kwargs.get("pk"))
#         serializer = ProductSerializer(instance=product, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#
#         return Response(serializer.data)
#
# # TODO: UpdateProductView
#
#
# class ProductListAPIView(generics.ListAPIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#
#         return Response(serializer.data)
#
#
#  TODO H/W:  ListCreateAPIView (CreateProductList)

class ProductViewSet(viewsets.ModelViewSet):
    """
    Descr.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def info(self, request):
        return Response({'info': 'Hello, World !'})

# permission_classes = [IsAccountAdminOrReadOnly]