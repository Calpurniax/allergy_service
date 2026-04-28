from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
import requests

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
        print("error")
        return Response(
             {"error":"Error al conectar con Google Sheets: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )   
    return Response(
                {"message": "Datos guardados correctamente"},
                status=status.HTTP_201_CREATED
            ) 

def getUserGsheet(data): 
    try:    
        sheet = openGsheet()  
        cell = sheet.find(data['email'])        
        data = sheet.row_values(cell.row)
        #estaria bien quitar espacios vacios por si hace cosas raras? o mirar que no haga cosas raras :)
        print(data)
        return data
       
    except Exception as e:
        print("error"+str(e))
        return Response(
             {"error":"Error al conectar con Google Sheets: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) 
