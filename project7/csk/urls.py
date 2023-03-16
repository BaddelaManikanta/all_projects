from django.urls import path
from csk.views import *

app_name='chennai'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('rayudu/',rayudu,name='rayudu'),
]