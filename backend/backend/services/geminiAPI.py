import json
from google import genai
from rest_framework.response import Response
from rest_framework import status

from .geminiKey import GEMINI_API_KEY

def geminiContext(user, weatherData): 
    
    context = {
        "request_type": "health_forecast_email",
        "user_profile": {
            "first_name": user[0],
            "city": user[3], 
            "language": "es"            
        },
        "air_quality_data": {
            "hourly": weatherData.get("hourly", {}),
            "units": weatherData.get("hourly_units", {})
        }
    }
    
    return context

def connectGemini(user, weatherResponse):    
    context = geminiContext(user, weatherResponse) 
    userPrompt = json.dumps(context, indent=2)

    client = genai.Client(api_key= GEMINI_API_KEY)

    systemPrompt = """
    Eres un experto en salud ambiental y bienestar. Tu función es analizar datos JSON de calidad del aire.
    Reglas de comportamiento:
    1. Analiza los niveles de PM2.5 y PM10 según los estándares de la OMS (Límite diario PM2.5: 15 µg/m³), analiza también los niveles de polen (el usuario si es alérgico, es alérgico a ese polen en concreto).
    2. Identifica tendencias en el pronóstico de 7 días (días más limpios vs. días más contaminados).
    3. Redacta emails empáticos, claros y con consejos médicos preventivos (ej. cuándo usar mascarilla, cuándo ventilar, cuándo evitar deporte).
    4. Usa un tono profesional pero cercano, dirigiéndote al usuario por su nombre.
    5. Estructura el email con: Asunto, Saludo, Resumen semanal, Calendario de salud y Despedida.
    """
    
    prompt = f"Genera el reporte de salud para el siguiente usuario y datos: {userPrompt}"
    try:
       response = client.models.generate_content(
            model="gemini-3.1-flash-lite-preview", 
            contents=prompt,
            config={
                'system_instruction': systemPrompt
            }
       )  
    except Exception as e:
        return Response(
             {"error":"Error al conectar con Gemini: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) 
    
    return response.text
