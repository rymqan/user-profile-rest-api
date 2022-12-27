from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Return list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as fucntion (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create hello message with name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def put(self, request, pk=None):
        """Handle object updating"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk=None):
        """Handle partial object updating"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """Delete object"""
        return Response({'method': 'DELETE'})
    
    
class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Return hello message"""
        
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create new hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self, request, pk=None):
        """Handle getting object"""
        return Response({'method': 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating object"""
        return Response({'method': 'PUT'})
    
    def partial_update(self, request, pk=None):
        """Handle updating object part"""
        return Response({'method': 'PATCH'})
        
    def destroy(self, request, pk=None):
        """Handle removing object"""
        return Response({'method': 'DELETE'})