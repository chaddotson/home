
from django.urls import path

from . import views

urlpatterns = [
    path('', views.summary, name='summary'),
    path('cameras/?', views.cameras, name='cameras'),
]