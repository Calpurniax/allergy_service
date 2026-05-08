from geopy.geocoders import Nominatim
from rest_framework.response import Response
from rest_framework import status

def getCoord(city):
    try:
        geolocator = Nominatim(user_agent="Allergy-ServiceApp")
        coordenates = geolocator.geocode(city)        
        return coordenates
    except Exception as e:
        return Response(
                    {"error":"Error al conectar con Nominatim: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                ) 