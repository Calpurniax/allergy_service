from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pathlib import Path
from django.conf import settings


def gDocsConnection():
    SCOPES = ['https://www.googleapis.com/auth/documents', 
              'https://www.googleapis.com/auth/drive']
   
    SERVICE_ACCOUNT_FILE = settings.GCREDENTIALS
    
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('docs', 'v1', credentials=creds), build('drive', 'v3', credentials=creds)

def generatePdfFromTemplate(text, userName):
    TEMPLATE_ID = settings.DOCS_TEMPLATE_ID
    try:
        docsService, drive_service = gDocsConnection()

        # Copiar la plantilla
        copy_body = {
            'name': f'Reporte_{userName}_{Path(__file__).stem}',
            'parents': [settings.GDRIVE_ID] #id de mi carpeta en Drive para evitar errores de "espacio no disponible" para service accounts
        }
        copied_file = drive_service.files().copy(fileId=TEMPLATE_ID, body=copy_body).execute()
        new_document_id = copied_file['id']

        # Escribir en la copia
        requests = [
            {
                'insertText': {
                    'location': {'index': 118}, 
                    'text': "\n" + text
                }
            }
        ]
        docsService.documents().batchUpdate(documentId=new_document_id, body={'requests': requests}).execute()

        
        pdf_path = Path(settings.BASE_DIR) / 'reports' / f'reporte_{userName}.pdf'
        pdf_path.parent.mkdir(parents=True, exist_ok=True)  # Crear directorio si no existe

        request = drive_service.files().export_media(fileId=new_document_id, mimeType='application/pdf')
        pdf_content = request.execute()

        with open(pdf_path, 'wb') as f:
            f.write(pdf_content)      

        return str(pdf_path), None

    except HttpError as e:
        return None, f"Error de Google API: {e.reason}"
    except Exception as e:
        return None, f"Error inesperado: {str(e)}"
