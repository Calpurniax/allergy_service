from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials
from rest_framework.response import Response
from rest_framework import status

def openGsheet():
    sheet = settings.GSCLIENT.open_by_key(settings.GSHEET_ID).sheet1
    return sheet

def appendRowToGsheet(row, sheet):
    sheet.append_row(row)

def createUserInGsheet(row):
    try:
        sheet=openGsheet()
        appendRowToGsheet(row, sheet)
        
    except Exception as e:
        return Response(
             {"error":"Error al conectar con Google Sheets: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    print("usuario creado")
    return Response(
                {"message": "Datos guardados correctamente"},
                status=status.HTTP_201_CREATED
            ) 

