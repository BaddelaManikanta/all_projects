from django.urls import path
from cricket.views import *

app_name='cricket'

urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('sachin/',sachin,name='sachin'),
]