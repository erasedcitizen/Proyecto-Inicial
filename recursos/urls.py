from django.urls import path
from . import views

urlpatterns = [
    path("", views.recursos, name="recursos"),
    path('derechos/', views.derechos_educacionales, name='derechos'),
]