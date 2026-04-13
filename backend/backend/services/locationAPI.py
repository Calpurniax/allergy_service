from geopy.geocoders import Nominatim

URL ='https://nominatim.openstreetmap.org/search?format=json&limit=1&q='

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