from rest_framework import generics


from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer
from backend.services.gsheet import appendRowToGsheet
from backend.services.gsheet import openGsheet
from backend.services.locationAPI import getCoord
# Create your views here.

class Userview(generics.CreateAPIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
      

        if serializer.is_valid():
            data = serializer.validated_data            
            coordenates = getCoord(data['location'])
            
            row = [
                data['name'],
                data['email'],
                data['birthdate'],
                data['location'],
                coordenates.latitude,
                coordenates.longitude,
                data['allergies'],
                data['password']
            ]

            try:
                sheet=openGsheet()
                appendRowToGsheet(row, sheet)
            except Exception as e:
                return Response(
                    {"error":"Error al conectar con Google Sheets: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )           

            return Response(
                {"message": "Datos guardados correctamente"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
