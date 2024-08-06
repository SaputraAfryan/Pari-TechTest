from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Books
from .serializers import BookSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class ListBooks(APIView):
    """
    Navigate to 'https://example.host/books/' 
    
    GET:
        Retrieve a list of all items.
    
    POST:
        Create a new item instance. The request body should contain the item detail.
    """
    
    @swagger_auto_schema(
        operation_description="Retrieve a list of all items.",
        responses={200: BookSerializer(many=True)}
    )
    
    def get(self, request, *args, **kwargs):
        book = Books.objects.all()
        serializer_class = BookSerializer(book, many=True)
        return Response(serializer_class.data)

    @swagger_auto_schema(
        operation_description="Create a new item instance. The request body should contain the item detail.",
        request_body=BookSerializer,
        responses={201: BookSerializer, 400: 'Bad Request'}
    )

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DetailBooks(APIView):
    """
    Navigate to 'https://example.host/books/{id}'

    GET:
        Retrieve item instance by ID.
        
    PUT:
        Update item instance by ID. The request body should contain the item detail.
        
    DELETE:
        Delete item instance by ID.
    """
    
    @swagger_auto_schema(
        operation_description="Retrieve item instance by ID.",
        responses={200: BookSerializer, 404: 'Not Found'}
    )

    def get(self, request, pk, *args, **kwargs):
        try:
            queryset = Books.objects.get(id=pk)
            serializer_class = BookSerializer(queryset)
            return Response(serializer_class.data)
        except queryset.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
      
    @swagger_auto_schema(
        operation_description="Update item instance by ID. The request body should contain the item detail.",
        request_body=BookSerializer,
        responses={200: BookSerializer, 400: 'Bad Request', 404: 'Not Found'}
    )  
    
    def put(self, request, pk, *args, **kwargs):
        try:
            book = Books.objects.get(id=pk)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer_class = BookSerializer(book, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="Delete item instance by ID.",
        responses={204: 'No Content', 404: 'Not Found'}
    )
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            book = Books.objects.get(id=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
