from rest_framework import generics, status

from .serializers import UserSerializer
from .userService import newUser
from rest_framework.response import Response


# Create your views here.

class Userview(generics.CreateAPIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)      

        if serializer.is_valid():
            data = serializer.validated_data           
            newUser(data)         
            return Response({"message": "usuario creado"}, status=status.HTTP_201_CREATED)          

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
