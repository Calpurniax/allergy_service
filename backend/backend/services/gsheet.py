from django.conf import settings
from oauth2client.service_account import ServiceAccountCredentials


def open_gsheet():
    sheet = settings.GSCLIENT.open_by_key(settings.GSHEET).sheet1
    return sheet

def append_row_to_gsheet(row, sheet):
    sheet.append_row(row)

