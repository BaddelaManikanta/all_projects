from django.urls import *
from football.views import *

app_name='football'

urlpatterns=[
    path('ronaldo/',ronaldo,name='ronaldo'),
    path('messi/',messi,name='messi'),
]