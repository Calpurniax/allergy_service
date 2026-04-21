from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.utils.html import strip_tags
import os


def sendEmail(userData, pdfPath=None):
    userName = userData[0]
    userEmail = userData[1]

    html_content = f"""
    <html>
    <body>
        <h1>Reporte de Salud Ambiental</h1>
        <p>Hola {userName},</p>
        <p>Adjunto encontrarás el reporte para esta semana en PDF.</p>
        <p>Saludos,<br>Equipo de Salud Ambiental</p>
    </body>
    </html>
    """
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject=f'Reporte de Salud Ambiental - {userName}',
        body= text_content, 
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[userEmail],
    )
    
    email.attach_alternative(html_content, "text/html")

    # Añadir attachment PDF si se proporciona la ruta
    if pdfPath and os.path.exists(pdfPath):
        email.attach_file(pdfPath)

    try:
        email.send()
        return True
    except Exception as e:
        print(f"Error enviando email: {e}")
        return False
