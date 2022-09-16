from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializers
import random
from .producer import publish
# Create your views here.


class ProductViewSet(viewsets.ViewSet):
    def list(self, res):  # /api/products
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)

    def create(self, res):  # /api/products
        serializer = ProductSerializers(data=res.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish(method='product_created', body=serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, res, pk=None):  # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    def update(self, res, pk=None):  # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializers(instance=product, data=res.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish(method='product_updated', body=serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, res, pk=None):  # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializers(instance=product, data=res.data)
        serializer.is_valid(raise_exception=True)
        deleted_data = serializer.data
        deleted_data["message"] = "deleted data"
        product.delete()
        publish(method='product_deleted', body=deleted_data)
        return Response(data=deleted_data, status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
