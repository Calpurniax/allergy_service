from django.core.mail import EmailMessage
from django.conf import settings


def sendEmail(userData, content):
    
    userName = userData[0]
    useEmail = userData[1]

    email = EmailMessage(
        subject=f'Reporte de Salud Ambiental - {userName}',
        body=content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[useEmail],
    )   

    try:
        email.send()
        return True
    except Exception as e:
        print(f"Error enviando email: {e}")
        return False
