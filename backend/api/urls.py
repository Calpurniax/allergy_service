
from django.urls import path
from .views import Userview, Emailview

urlpatterns = [
    path('user/', Userview.as_view()),
    path('send-email/', Emailview.as_view())    
]