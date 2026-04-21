from rest_framework.response import Response
from rest_framework import status

from backend.services.locationAPI import getCoord
from backend.services.gsheet import createUserInGsheet
from backend.services.weatherAPI import callweatherAPI
from backend.services.geminiAPI import connectGemini
from backend.services.gdocs import generatePdfFromTemplate
from backend.services.emailService import sendEmail

def createRow(data):
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
    return row  

def newUser(data):
    row = createRow(data)
    createUserInGsheet(row)      
    userLat = row[4]
    userLong = row[5]
    weather = callweatherAPI(userLat, userLong)         
    docForEmail = connectGemini(row, weather) 
    pdfPath, error = generatePdfFromTemplate(docForEmail, row[0])  # row[0] es userName
    if error:
        print(f"Error generando PDF: {error}")
        sendEmail(row, '')   
        return Response({"error": "Error generando PDF"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    sendEmail(row, pdfPath)   

   



