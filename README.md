# allergy_service
Full stack app for allergy and air quality info

## Future features

### Frontend 

[ ] Error and success messages

[ ] Input validation

[x] Allergies as a select/multichoice

[ ] More values for get a specific location (like Country for ex.)

### Backend 

[x] Add google docs connection (create template, export PDF)

[x] Create email content with HTML and send the PDF as attachment

[x] Manage allergies 

[x] Create an ID for the users

[x] Hash password to save them properly in db

## Enviroment variables for the project

DOCS_TEMPLATE_ID = the ID for a template in google docs
GSHEET_ID = the google sheet ID for the database
GDRIVE_ID = The google drive ID for creating the PDF files 

EMAIL_HOST_USER= your e-mail
EMAIL_HOST_PASSWORD=password for your e-mail
DEFAULT_FROM_EMAIL=your e-mail

SECRET_KEY = django secret key

