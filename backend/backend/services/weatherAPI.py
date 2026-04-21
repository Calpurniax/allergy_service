import requests
from rest_framework.response import Response
from rest_framework import status

weatherAPI ='https://air-quality-api.open-meteo.com/v1/air-quality?'


def callweatherAPI (lat, long, allergy, forecast_days):
    try:
        url = f"{weatherAPI}forecast_days={forecast_days}&latitude={lat}&longitude={long}&hourly=pm10,pm2_5,{allergy}"           
        response = requests.get(url)   
        print(url)        
        data =response.json()
        return data
    except Exception as e:
       
        return Response(
                    {"error":"Error al conectar con air-quality-api: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                ) 