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

def createRow(data):
    coordenates = getCoord(data['location'])
    userID = str(uuid.uuid4())[:8]
    hashedPassword = make_password(data['password'])
    row = [
                userID,
                data['name'],
                data['email'],
                data['birthdate'],
                data['location'],
                coordenates.latitude,
                coordenates.longitude,
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
        #print(weather)     
        docForEmail = connectGemini(userName, userCity, weather)        
        pdfPath, error = generatePdfFromTemplate(docForEmail, userName)
        if error:
            print(f"Error generando PDF: {error}")
            sendEmail(userName, userEmail, '')   
            return Response({"error": "Error generando PDF"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        sendEmail(userName, userEmail, pdfPath)




