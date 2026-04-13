from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials

def openGsheet():
    sheet = settings.GSCLIENT.open_by_key(settings.GSHEET).sheet1
    return sheet

def appendRowToGsheet(row, sheet):
    sheet.append_row(row)

