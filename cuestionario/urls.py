from django.urls import path
from .views import cuestionariopaso1, cuestionariopaso2, descarga

urlpatterns = [
    path('', cuestionariopaso1, name='cuestionario'),
    path('2/', cuestionariopaso2, name='paso2'),
    path('descarga/', descarga, name='descarga'),
]