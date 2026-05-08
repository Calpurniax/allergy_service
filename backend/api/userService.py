from rest_framework.response import Response
from rest_framework import status
import uuid
from django.contrib.auth.hashers import make_password

from backend.services.locationAPI import getCoord
from backend.services.gsheet import createUserInGsheet, getUserGsheet
from backend.services.weatherAPI import callweatherAPI
from backend.services.geminiAPI import connectGemini
from backend.services.gdocs import generatePdfFromTemplate
from backend.services.emailService import sendEmail
from math import floor


def createRow(data):
    coordenates = getCoord(data['location'])  
    #weather API da error si mandas coordenadas con más de 2 decimales  
    latitude = (floor(coordenates.latitude * 100)/100)
    longitude = (floor(coordenates.longitude*100)/100)
    userID = str(uuid.uuid4())[:8]
    hashedPassword = make_password(data['password'])
    row = [
                userID,
                data['name'],
                data['email'],
                data['birthdate'],
                data['location'],
                latitude,
                longitude,
                data['allergies'],
                hashedPassword,                
            ]
    return row  

def newUser(data):
    row = createRow(data)
    createUserInGsheet(row)    

def createAndSendEmail(data):        
        row = getUserGsheet(data) 
        userName =row[0] 
        userEmail = row[1]  
        userCity= row[3]
        userLat = row[5]
        userLong = row[6]
        userAllergy = row[7]
        weather = callweatherAPI(userLat, userLong, userAllergy, forecast_days=7)    
        docForEmail = connectGemini(userName, userCity, weather)        
        pdfPath, error = generatePdfFromTemplate(docForEmail, userName)
        if error:
            print(f"Error generando PDF: {error}")
            sendEmail(userName, userEmail, '')   
            return Response({"error": "Error generando PDF"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        sendEmail(userName, userEmail, pdfPath)




