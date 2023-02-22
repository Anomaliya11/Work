from django.urls import path
from web_lib.views import main

urlpatterns = [
    path('', main, name='web_lib'),
    
]