import requests
from rest_framework.response import Response
from rest_framework import status

weatherAPI ='https://air-quality-api.open-meteo.com/v1/air-quality?hourly=pm10,pm2_5&'


def callweatherAPI (lat, long):
    try:
        url = f"{weatherAPI}latitude={lat}&longitude={long}"        
        response = requests.get(url)   
        data = response.json()   
        return data
    except Exception as e:
        return Response(
                    {"error":"Error al conectar con air-quality-api: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                ) 